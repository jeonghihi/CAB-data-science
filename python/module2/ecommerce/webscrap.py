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