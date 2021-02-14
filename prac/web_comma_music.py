from bs4 import BeautifulSoup
import urllib.request
import csv 
from urllib.error import URLError, HTTPError

list_bands = ['Crumb', 
'Cyndi+Lauper', 
'Daughter', 
'Dean+Blunt', 
'Delta+5', 
'Diamond+Thug', 
'Dives', 
'Dry+Cleaning', 
'Ellie+Goulding', 
'Emma+Ruth+Rundle', 
'eskimeaux', 
'Ex:Re', 
'Exploded+View', 
'First+Aid+Kit', 
'Frankie+Cosmos', 
'Garbage', 
'Girl+in+red', 
'Guano+Apes', 
'Halestorm', 
'Hole', 
'Holly+Throsby', 
'HTRK', 
'Hydrogen+Sea', 
'IAN+SWEET', 
'Jacqueline+Taieb', 
'Jealous', 
'Jennylee', 
'Jessica+Pratt', 
'Joan+Jett', 
'Joanne+Robertson', 
'Joy+Denalane', 
'Julia+Jacklin', 
'Juniore', 
'Kimbra', 
'L7', 
'La+Femme', 
'Laura+Carbone', 
'Lights', 
'Lilla+Clara', 
'Los+Bitchos', 
'LP', 
'Lucia', 
'Lucy+Dacus', 
'Lush', 
'Marie+Fisker', 
'Marriages', 
'Mary+Ocher', 
'Mazzy+Star', 
'Melanie+De+Biasio', 
'Melissa+Etheridge', 
'Men+I+Trust', 
'Missing+Persons', 
'Ndidi+O', 
'No+Doubt', 
'Noga+Erez', 
'North+Dakota', 
'Nouvelle+Vague', 
'Over+the+Rhine', 
'Patti+Smith', 
'Pip+Blom', 
'PJ+Harvey', 
'Pleasure+Symbols', 
'Porridge+Radio', 
'Postiljonen', 
'Project+Mama+Earth', 
'Room306', 
'Saint+Etienne', 
'Savages', 
'Screaming+Females', 
'Second+Still', 
'Sharon+Van+Etten', 
'Shiny+Toy+Guns', 
'Sibylle+Baier', 
'Siouxsie+and+the+Banshees', 
'Sixth+June', 
'Snail+Mail', 
'Sneaks', 
'Sofia+Portanet', 
'Sorry', 
'Squirrel+Flower', 
'Stereolab', 
'Still+Corners', 
'Stonefield', 
'Subtle+Pride', 
'Sunflower+Bean', 
'Tash+Sultana', 
'Tellavision', 
'Tess+Parks', 
'The+Aces', 
'The+Big+Moon', 
'The+BSMNT', 
'The+Courtneys', 
'The+Cranberries', 
'The+Dandelion', 
'The+Dead+Weather', 
'The+Distillers', 
'The+Innocence+Mission', 
'The+Kills', 
'The+Mynabirds', 
'The+Pierces', 
'The+Preatures', 
'The+Pretty+Reckless', 
'The+Raincoats', 
'The+Raveonettes', 
'The+Regrettes', 
'The+Slits', 
'The+Wild+Reeds', 
'This+Mortal+Coil', 
'Thunderpussy', 
'Tove+Lo', 
'Trixie+Whitley', 
'Unloved', 
'Valerie+June', 
'Vendredi+sur+Mer', 
'Vera', 
'Voodoo+Beach', 
'Warhaus', 
'Warpaint', 
'Waxahatchee', 
'Within+Temptation', 
'Wolf+Alice', 
'Yasmine+Hamdan', 
'Yeah+Yeah+Yeahs', 
'Young+Summer', 
'ZZ+Ward', 
'KATE+BOY', 
'Joss+Stone', 
'Tracy+Chapman']

list_urls = []

for item in list_bands:
  item = item.replace(' ','')
  URL = 'https://www.last.fm/music/' + item
  list_urls.append(URL)


#--- find bad url
def find_bad_qn(url):
    URL = url
    try:
        urllib.request.urlopen(URL)
    except:
        print('error happenend_' + URL)
        pass

print("Please Wait.. it will take some time")
for url in list_urls:
    find_bad_qn(url)

#=====
for url in list_urls:
    URL = url
    get_text(URL)


def get_text(URL):
    url_name = URL[26:]
    source_code_from_URL = urllib.request.urlopen(URL)   
    try:        
        print(source_code_from_URL)
    except HTTPError:
        print("HTTPError happened")
        pass
    else:
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
        text = ''
        for item in soup.find_all("li", {"class": "tag"}): 
            text = text + str(item.find_all(text=True)).replace('\\n', '')
        url_name = url_name.replace("+","_")
        my_file = str('C:/Users/Jeong/Downloads/result/text_res_' + url_name + '.csv')
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
import csv 

os.chdir("C:/Users/Jeong/Downloads/result/")

extension = 'csv'
all_filenames = [("C:/Users/Jeong/Downloads/result/"+i) for i in glob.glob('*.{}'.format(extension))]

res = []

for f in all_filenames:
    with open(f, 'r') as csv_file:        
        csv_reader= csv.reader(csv_file) #, delimiter=','
        for row in csv_reader:
            row = ''.join(row)
            result = f[32:] + "_" + row
            res.append(result)

res

# data to be written row-wise in csv fil 
# opening the csv file in 'w' mode and writing the data into the file 

with open('C:/Users/Jeong/Downloads/result/res_all_4.csv', 'w', newline ='') as f: #
    write = csv.writer(f)
    for item in res:
        write.writerow([item])

# httperror related: https://im-coder.com/urllib2-try-und-except-auf-404.html
# https://stackoverflow.com/questions/1726402/in-python-how-do-i-use-urllib-to-see-if-a-website-is-404-or-200
# https://stackoverflow.com/questions/3465704/python-urllib2-urlerror-http-status-code
# https://stackoverflow.com/questions/23715815/python-urlopen-skip-entry-if-any-error-occurs
