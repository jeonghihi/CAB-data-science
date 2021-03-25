---
# title : "python-module2-week9-email1"
# date : "2021-03-24"
# tags : [python, ecommerce]
---

# competitive analysis

- research on competitors (start-up, mid/big ones)
    - identify competitors and evaluate their strategies to determine their strengths (e.g. popular products, ADs strategy) and weaknesses (e.g. when sales volume is low, high shiping cost for some regions) compared to your own business, product and service.
- to gather insights necessary to find/develop go-to-market strategy.

# webscrap
- try the package "beautifulsoup" and follow [this tutorial](https://www.pluralsight.com/guides/web-scraping-with-beautiful-soup) and [this](https://realpython.com/beautiful-soup-web-scraper-python/). 
- xpath [tutorial](https://www.zyte.com/blog/an-introduction-to-xpath-with-examples/#:~:text=XPath%20is%20a%20powerful%20language,extract%20web%20data%20using%20Scrapy.&text=Just%20paste%20the%20HTML%20samples,and%20play%20with%20the%20expressions.)

- more details about python webscraping in this [book](https://yanfei.site/docs/dpsa/references/PyWebScrapingBook.pdf)
- another [resource] about web scraping(https://automatetheboringstuff.com/2e/chapter12/)

- task: extract basic information - Name of the product, size, review count and rating etc.

- Answer questions (for learning report).
## Briefly describe the differences between the webbrowser, requests, bs4. (hint : You can choose to elaborate your understanding visually by making diagrams)
- webbrowser is used to browse World Wide Web by retrieving the requested data from the webserver that the webiste is hoseted on (i.e. open a webpage).
- requests is used to request the data from server and fetch the requested data (responses from the server) in a big chunk of text format (HTML). (i.e. download a webpage).
- bs4(beautifulsoup4) is used to translate/parses the HTML text and allow the user to search/access to elements within HTML text. (i.e. read html page).

## How web scraping is related / not-related to Data Mining and API ?
- The accuracy of web-scraping could influences the quality of database (across all steps, from the data pre-processing and to the application).
- The efficiency of web-scraping could facilitate/hinder the development of API.
- Depending on the type of database (e.g., static/dynamic), the role of web-scraping could be less important once the collected (& preprocessed) data via web scraping is implemented.

## Do you think if you send huge number of requests to a web page, there is a good chance the server denies your further request.
- yes. there would be also limit depending on how quickly this requests are sent. so we can combine "time" method and "headers (by creating random_user_agent)"

## Can you think of such scenarios which will hinder your web scraping activity.
- html with a complex structure. e.g., floating(hidden) objects called via function/script 
- [anti-bot technique(system)][2] e.g., Browser fingerprinting, IP-rate limiting, CAPTCHAs

## Can you think of few other business models which are based on web scraping.
- web scraping tool/software e.g., paid web-scraping [services][3] 

## What type of object is returned by requests.get()? How can you access the downloaded content as a string value ?
- the object returned by requests.get() is _response_ : "requests.models.Response". 
- we can access to the contents by _response.text_

## What requests method checks that the download worked ?
```python
url = "https://stackoverflow.com"
response = requests.get(url, stream=True)
response
```

## How can you get the HTTP status code of a requests response ?
```python
import requests
try:
    r = requests.head("https://stackoverflow.com")
    print(r.status_code)
    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")
```

## How do you save a requests response to a file ?
- save as a text file.
```python
# Request the HTML for this web page:
response = requests.get("https://stackoverflow.com/questions/31126596/saving-response-from-requests-to-file")
with open("response.txt", "w") as f:
    f.write(response.text)
```
- [code examples][6]


[2]: https://www.scrapingbee.com/blog/web-scraping-without-getting-blocked/

[3]: https://www.scrapehero.com/top-free-and-paid-web-scraping-tools-and-software/

[5]: https://scrapingpass.com/blog/web-scraping-and-data-preprocessing/ https://www.statworx.com/ch/blog/web-scraping-101-in-python-with-requests-beautifulsoup/ https://www.journaldev.com/44473/scrape-amazon-product-information-beautiful-soup

[6]: https://stackoverflow.com/questions/31126596/saving-response-from-requests-to-file

[display the speed/progress bar of downloads]: https://stackoverflow.com/questions/15644964/python-progress-bar-and-downloads/15645088#15645088 https://stackoverflow.com/questions/20801034/how-to-measure-download-speed-and-progress-using-requests

https://stackoverflow.com/questions/27652543/how-to-use-python-requests-to-fake-a-browser-visit-a-k-a-and-generate-user-agent
