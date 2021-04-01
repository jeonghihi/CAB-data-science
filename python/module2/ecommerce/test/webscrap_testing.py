webscrap.py

#%%
tuple = {}
tuple[(1,2,4)]=8
tuple[(4,2,1)]=10
tuple[(1,2)]=12
_sum = 0
for k in tuple:
    _sum + tuple[k]

print(len(tuple)+_sum)

#%% plans
# relative/absolute path: https://stackoverflow.com/questions/918154/relative-paths-in-python

# base: 'https://www.amazon.de/s?k=Monitor&ref=nb_sb_noss'

# pages:
# "/-/en/s?k=Monitor&amp;qid=1616750311&amp;ref=sr_pg_1
# "/-/en/s?k=Monitor&amp;page=2&amp;qid=1616750311&amp;ref=sr_pg_2"
# "/-/en/s?k=Monitor&amp;page=2&amp;qid=1616750311&amp;ref=sr_pg_3"
# "/-/en/s?k=Monitor&amp;page=3&amp;qid=1616750311&amp;ref=sr_pg_4"

#1 - at main: links to first10pages 
Create search.yml

#2 - at each page: title, ratingNr, price of products listed in each page and links to product-pages
title: (span: "a-size-medium a-color-base a-text-normal" ), raingNr (span class="a-size-base") 
(span class="a-icon-alt") in (div class="a-row-a-size-small")
, price (span:"a-price-whole")
#3 - at each product page: ratings + freq combi (?),  similar items (ratings stars/nr)
(span: "a-size-base") in (table: "histogramTable") 
in (div: "a-fixed-left-grid-col a-col-left") in (div: reviewsMedley)

#%% read yaml
import yaml 
filepath = 'envs/CAB/CAB-data-science/CAB-data-science/python/module2/ecommerce/pipe/search.yml'
with open(filepath, 'r') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    products = yaml.load(file, Loader=yaml.FullLoader)
    print(products)

# what is different between 'r' and 'w+' : w+ is writing in a new file (if file did not exist before)
# jsonlint - to check json file

#%% write and read yaml 

import yaml
import pprint
 
def read_yaml():
    """ A function to read YAML file"""
    with open('configs.yml') as f:
        config = list(yaml.safe_load_all(f))
 
    return config
 
def write_yaml(data):
    """ A function to write YAML file"""
    with open('toyaml.yml', 'a') as f:
        yaml.dump_all(data, f, default_flow_style=False)
 
if __name__ == "__main__":
 
    # read the config yaml
    my_config = read_yaml()
 
    # pretty print my_config
    pprint.pprint(my_config)
 
    # write A python object to a file
    write_yaml(my_config)

# dict basic: https://www.programiz.com/python-programming/nested-dictionary
# convert between yaml and dict: https://cyruslab.net/2020/02/05/python-convert-dictionary-to-yaml-and-vice-versa/
# save dict to csv/json : https://pythonspot.com/save-a-dictionary-to-a-file/

#%%
# data extraction and cleaning

# codesource: https://www.journaldev.com/44473/scrape-amazon-product-information-beautiful-soup
HEADERS = ({'User-Agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            'Accept-Language': 'en-US, en;q=0.5'})

base_url = 'https://www.amazon.de/'
item_url = '-/en/Portable-Monitor-Corprit-Mini-HDMI-Protective/dp/B089LNM5HP/ref=sr_1_20?dchild=1&amp;keywords=Monitor&amp;qid=1616750441&amp;sr=8-20'
full_url = base_url + item_url
webpage = requests.get(full_url, headers=HEADERS)
soup = BeautifulSoup(webpage.content,  "html.parser")
# soup.prettify()

# Outer Tag Object
title = soup.find("span", attrs={"class":'a-size-medium a-color-bas a-text-normal'})

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
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
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

#%%
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


each product page has sdifferent structure:
product summary
product detail
product info > technical details

#https://www.amazon.de/-/en/Acer-Nitro-23-8Zoll-Schwarz-Computerbildschirm/dp/B07C5H9NDT/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1

#https://www.amazon.de/Samsung-T35F-IPS-Monitor-1080p-Randlos/dp/B08C7VBC81/ref=sr_1_26?dchild=1&keywords=Monitor&qid=1617015152&sr=8-26

