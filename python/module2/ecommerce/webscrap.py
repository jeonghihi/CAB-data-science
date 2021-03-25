# source: https://www.pluralsight.com/guides/web-scraping-with-beautiful-soup

# install packages
pip install beautifulsoup4 requests

#%%
# install modules
from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests

#%%
# data extraction and cleaning

# codesource: https://www.journaldev.com/44473/scrape-amazon-product-information-beautiful-soup
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

URL = 'https://www.amazon.de/-/en/Raspberry-ARM-Cortex-A72-WLAN-ac-Bluetooth-Micro-HDMI-Single/dp/B07TC2BK1X/ref=sr_1_3?dchild=1&keywords=Raspberry+Pi&qid=1616587962&sr=8-3'
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content,  "html.parser")

# Outer Tag Object
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
 
# Printing Product Title
print("Product Title = ", title_string)
# %% scrap product size & review counts 

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

URL = 'https://www.amazon.de/-/en/Raspberry-ARM-Cortex-A72-WLAN-ac-Bluetooth-Micro-HDMI-Single/dp/B07TC2BK1X/ref=sr_1_3?dchild=1&keywords=Raspberry+Pi&qid=1616587962&sr=8-3'
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content,  "html.parser")

# Outer Tag Object
features = soup.find("div", attrs={"id":'detail-bullets_feature_div'})
rows = features.find_all('span')

features_text = []
for row in rows:
    info_raw = row.get_text()
    info_val = info_raw.replace('\n','')
    features_text.append(info_val)

print(features_text) 

#%% logger 

import logging

class Logger:
    def __init__(self):
        # Initiating the logger object
        self.logger = logging.getLogger(__name__)
        
        # Set the level of the logger. This is SUPER USEFUL since it enables you to decide what to save in the logs file.
        # Explanation regarding the logger levels can be found here - https://docs.python.org/3/howto/logging.html
        self.logger.setLevel(logging.DEBUG)
        
        # Create the logs.log file
        handler = logging.FileHandler('logs.log')

        # Format the logs structure so that every line would include the time, name, level name and log message
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        # Adding the format handler
        self.logger.addHandler(handler)
        
        # And printing the logs to the console as well
        self.logger.addHandler(logging.StreamHandler(sys.stdout))

# Usage example:
logger = Logger().logger
logger.debug("This log's level is 'DEBUG'")
logger.info("This log's level is 'info'")
logger.error("This log's level is 'error'")
#%%
from fake_useragent import UserAgent

def random_header(logger):
    # Create a dict of accept headers for each user-agent.
    accepts = {"Firefox": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Safari, Chrome": "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5"}
    
    # Get a random user-agent. We used Chrome and Firefox user agents.
    # Take a look at fake-useragent project's page to see all other options - https://pypi.org/project/fake-useragent/
    try: 
        # Getting a user agent using the fake_useragent package
        ua = UserAgent()
        if random.random() > 0.5:
            random_user_agent = ua.chrome
        else:
            random_user_agent = ua.firefox
    
    # In case there's a problem with fake-useragent package, we still want the scraper to function 
    # so there's a list of user-agents that we created and swap to another user agent.
    # Be aware of the fact that this list should be updated from time to time. 
    # List of user agents can be found here - https://developers.whatismybrowser.com/.
    except FakeUserAgentError as error:
        # Save a message into a logs file. See more details below in the post.
        logger.error("FakeUserAgent didn't work. Generating headers from the pre-defined set of headers. error: {}".format(error))
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"]  # Just for case user agents are not extracted from fake-useragent package
        random_user_agent = random.choice(user_agents)
    
    # Create the headers dict. It's important to match between the user-agent and the accept headers as seen in line 35
    finally:
        valid_accept = accepts['Firefox'] if random_user_agent.find('Firefox') > 0 else accepts['Safari, Chrome']
        headers = {"User-Agent": random_user_agent,
                  "Accept": valid_accept}
    return headers

#%%
my_Headers = random_header(logger)
#%% full process with random_user

import requests    
# set headers to be recognized as human activity
# this random_header gives me error
#my_Headers = random_header(logger)

my_HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# target url 
my_URL = 'https://www.amazon.de/-/en/Raspberry-ARM-Cortex-A72-WLAN-ac-Bluetooth-Micro-HDMI-Single/dp/B07TC2BK1X/ref=sr_1_3?dchild=1&keywords=Raspberry+Pi&qid=1616587962&sr=8-3'

def load_webpage(URL, HEADERS):
    # load the webpage
    try:
        r = requests.head(URL, headers=HEADERS)
        status = r.status_code
        # prints the status code. Find more at httpstatusrappers.com :)
        if status == 200:
            webpage = requests.get(URL, headers=HEADERS)
            result = webpage
        else:
            result = print("failed code",status)
    except requests.ConnectionError:
        result = print("failed to connect")

    return result

load_webpage(my_URL, my_HEADERS)
#%% without random_user
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

    # scrap the target object(contents)
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
    write.writerows([features_text])
#%%

    #clean_url
    def remove(string_input): 
        return "".join(string_input.split()) 
    out_URL = remove(my_URL)


#%%
# parse the webpage

# Request the HTML for this web page:
response = requests.get("https://stackoverflow.com/questions/31126596/saving-response-from-requests-to-file")
with open("response.txt", "w") as f:
    f.write(response.text)


#%% Arun's example

import requests # Import requests
from bs4 import BeautifulSoup # Import BeautifulSoup4

# Windows 10 with Google Chrome
user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
'Safari/537.36'

headers = { 'User-Agent': user_agent_desktop}

url_twitter = 'https://www.amazon.com/Sony-MDRZX110-BLK-Stereo-Headphones/dp/B00NJ2M33I/ref=sr_1_3?dchild=1&keywords=headphones&qid=1616593900&sr=8-3'
resp = requests.get(url_twitter, headers=headers)  # Send request

code = resp.status_code  # HTTP response code
if code == 200:
    soup = BeautifulSoup(resp.text, 'lxml')  # Parsing the HTML
    print(soup.prettify())
else:
    print(f'Error to load Twitter: {code}')
# %%
