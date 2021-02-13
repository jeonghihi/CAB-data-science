from bs4 import BeautifulSoup
import urllib.request
import csv 

list_bands = ['Sleater+Kinney','Ssion','St.+Vincent','Sugababes','Sylvan+Esso','The+Cardigans','Trampauline','Tropic+of+Cancer','Thievery+Corporation','SASSY+009','AnnaMelina','Catnapp','Jasper+Lotti','Blondie','Carla+dal+Forno','Cat+Power','Charlotte+Gainsbourg','Christina+Aguilera','CHVRCHES','Anita+Baker','Aretha+Franklin','Duffy','Iyeoka','Jorja+Smith','Lianne+LaHavas','Marlena+Shaw','Melody+Gardot','Rachael+Yamagata','Sade','Stacey+Kent','Sophie+Milman','Strange+Fruit','Tango+with+Lions','The+Transatlantics','Moloko','Norah+Jones','Beth+Hart','070+Shake','A+Place+To+Bury+Strangers','Abra','Angel+Haze']
list_urls = []

for item in list_bands:
  item = item.replace(' ','')
  URL = 'https://www.last.fm/music/' + item
  list_urls.append(URL)

for url in list_urls:
    URL = url
    get_text(URL)


def get_text(URL):
    url_name = URL[26:]
    source_code_from_URL = urllib.request.urlopen(URL)
    print(source_code_from_URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all("li", {"class": "tag"}): 
        text = text + str(item.find_all(text=True)).replace('\\n', '')
    url_name = url_name.replace("+","_")
    my_file = str('C://Users/Jeong/CAB/CAB-data-science/result/text_res_' + url_name + '.csv')
    print(my_file)
    with open(my_file, 'w') as csv_file:        
        csv_writer = csv.writer(csv_file) #, delimiter=','
        csv_writer.writerow(text)

    return text

    

# soup.find_all("div", {"class": "buffer-standard"}): #section', class='catalogue-tags'
#.splitlines() #.rstrip("\n") #.replace('\\n', '')
  #URL = 'https://bandcamp.com/search?q=' + item


## merge csv files into one csv

import os
import glob
import pandas as pd
os.chdir("C:/Users/Jeong/CAB/CAB-data-science/result")

extension = 'csv'
all_filenames = [("C:/Users/Jeong/CAB/CAB-data-science/result/"+i) for i in glob.glob('*.{}'.format(extension))]

import csv 

res = []

for f in all_filenames:
    with open(f, 'r') as csv_file:        
        csv_reader= csv.reader(csv_file) #, delimiter=','
        for row in csv_reader:
            row = ''.join(row)
            result = f[52:] + "_" + row
            res.append(result)

res
#export to csv
res.to_csv( "combined_res.csv", index=False, encoding='utf-8-sig')
