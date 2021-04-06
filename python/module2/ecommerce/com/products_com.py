#%% import fake_useragent
from selectorlib import Extractor
import requests
from fake_useragent import UserAgent
from fake_useragent import FakeUserAgentError
import random

import json
from time import sleep

# Create an Extractor by reading from the YAML file
# my_dir = "python/module2/ecommerce/pipe/"

def random_header():
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
    except FakeUserAgentError:
        # Save a message into a logs file. See more details below in the post.
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"]  # Just for case user agents are not extracted from fake-useragent package
        random_user_agent = random.choice(user_agents)
    
    # Create the headers dict. It's important to match between the user-agent and the accept headers as seen in line 35
    valid_accept = accepts['Firefox'] if random_user_agent.find('Firefox') > 0 else accepts['Safari, Chrome']
    headers = {"User-Agent": random_user_agent,
                "Accept": valid_accept}
    return headers

def scrape(url):
    # load yml for data extraction
    e = Extractor.from_yaml_file('products_com.yml')

    # load random header info using  function random_header()
    random_header_info = random_header()

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': list(random_header_info.values())[0],
        'accept': list(random_header_info.values())[1],
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code != 200:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)

def create_product_output(item):
    # product_data = []
    with open("./output/product_urls_com_" + item + "_4.txt",'r') as urllist, open('./output/product_output_com_' + item + '_4.jsonl','w+') as outfile:
        for url in urllist.read().splitlines():
            data = scrape(url) 
            if data:
                try:
                    data['seller_link'] = 'https://www.amazon.com' + data['seller_link']
                    data['freq_bought_link'] = 'https://www.amazon.com' + data['freq_bought_link']
                    data['link_to_all_reviews'] = 'https://www.amazon.com' + data['link_to_all_reviews']
                    data['seller_link2'] = 'https://www.amazon.com' + data['seller_link2']
                    json.dump(data,outfile)
                    outfile.write("\n")
                except:
                    json.dump(data,outfile)
                    outfile.write("\n")

            sleep(.200)
    return outfile

#%%
item = "Monitor"
create_product_output(item)
sleep(2.500)




#%% 
# item = ['laptop']
category = ['DSLR+Camera','smartphone','laptop', 'mouse', 'keyboard','headphones'] 

for item in category:
    create_product_output(item)