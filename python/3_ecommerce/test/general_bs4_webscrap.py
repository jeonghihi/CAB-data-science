# source: https://www.pluralsight.com/guides/web-scraping-with-beautiful-soup

# install packages
pip install beautifulsoup4 requests

#%% full process with random_user

# install modules
from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests
import csv 
from datetime import datetime

# 1 # send requests to target URL with Headers
my_HEADERS = ({'User-Agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            'Accept-Language': 'en-US, en;q=0.5'})

my_URL = 'https://www.amazon.de/-/en/Raspberry-ARM-Cortex-A72-WLAN-ac-Bluetooth-Micro-HDMI-Single/dp/B07TC2BK1X/ref=sr_1_3?dchild=1&keywords=Raspberry+Pi&qid=1616587962&sr=8-3'

raw_contents = requests.get(my_URL, headers=my_HEADERS)
print(raw_contents)

# 2 # scrap data if webpage is not nonetype
if type(raw_contents.text) == str:
    # parse the webpage using soup
    webpage = raw_contents
    soup = BeautifulSoup(webpage.content,  "html.parser")

    title = soup.find("span", attrs={"id":'productTitle'})

    # Inner NavigableString Object
    title_value = title.string

    # Title as a string value
    title_string = title_value.strip()

    # Printing types of values for efficient understanding
    print(type(title))
    print(type(title_value))
    print(type(title_string))
    print()

    # scrap the target object(more contents)
    features = soup.find("div", attrs={"id":'detail-bullets_feature_div'})
    rows = features.find_all('span')

    features_text = []
    for row in rows:
        info_raw = row.get_text()
        info_val = info_raw.replace('\n','')
        features_text.append(info_val)

    print(features_text) 
else:
    print('no data from HTML')

# 3 # save the results with timestamp to text file 
# Returns a datetime object with local date and time
dateTimeObj = datetime.now() 
# Converting datetime object to string
timestampStr = dateTimeObj.strftime("%Y-%b-%d_%H-%M-%S_%f")

output_path = "./output/response_" + timestampStr + "msec.txt"

with open(output_path, "w", newline='') as f:
    #identify headers
    header = ['URL', 'StatusCode', 'Response']
    writer = csv.DictWriter(f, fieldnames = header)
    writer.writeheader()

    # writing data row-wise into the csv file
    write = csv.writer(f, quotechar =',',quoting=csv.QUOTE_MINIMAL)
    write.writerow([my_URL])
    write.writerow([webpage.status_code])
    write.writerow([title_string])
    write.writerows([features_text])
# %%
