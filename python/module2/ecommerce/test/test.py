#%% creating proxy pool

def proxies_pool():
    url = 'https://www.sslproxies.org/'
    
    # Retrieve the site's page. The 'with'(Python closure) is used here in order to automatically close the session when done
    with requests.Session() as res:
        proxies_page = res.get(url)
        
    # Create a BeutifulSoup object and find the table element which consists of all proxies
    soup = BeautifulSoup(proxies_page.content, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')
  
    # Go through all rows in the proxies table and store them in the right format (IP:port) in our proxies list
    proxies = []
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append('{}:{}'.format(row.find_all('td')[0].string, row.find_all('td')[1].string))
    return proxies

res = proxies_pool()
print(res)

#%%
import requests
try:
    r = requests.head("https://stackoverflow.com")
    print(r.status_code)
    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")

# %%
response = requests.get("https://stackoverflow.com/questions/31126596/saving-response-from-requests-to-file")
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

# %%
# without Headers, the request is recognized as non-human activity (response: 503)
url = 'https://www.amazon.de/-/en/Raspberry-ARM-Cortex-A72-WLAN-ac-Bluetooth-Micro-HDMI-Single/dp/B07TC2BK1X/ref=sr_1_3?dchild=1&keywords=Raspberry+Pi&qid=1616587962&sr=8-3'
response = requests.get(url, stream=True)
response
# %%
# with Headers, the request is recognized as normal activity (response: 200)
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
url = 'https://www.amazon.de/-/en/Raspberry-ARM-Cortex-A72-WLAN-ac-Bluetooth-Micro-HDMI-Single/dp/B07TC2BK1X/ref=sr_1_3?dchild=1&keywords=Raspberry+Pi&qid=1616587962&sr=8-3'
response = requests.get(url, stream=True, headers=HEADERS)
response