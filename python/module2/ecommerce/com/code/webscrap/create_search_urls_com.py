#%% specific item in one category
item = 'Headphones'
category = 'electronics'

f = open('search_urls_com_' + item + '.txt', 'w+')
for i in range(1,150):
    page_url = 'https://www.amazon.com/s?k=' + item + '&i=' + category + '&page=' + str(i) + '&language=en&ref=sr_pg_' + str(i)
    f.write(page_url)
    f.write('\n')
f.close()

# if products has less than 10 pages, find number of pages of the products
# (div class= "a-section a-spacing-small a-spacing-top-small")
# <div class="a-section a-spacing-small a-spacing-top-small"><span dir="auto">1-16 of over 2,000 results for</span><span dir="auto"> </span><span class="a-color-state a-text-bold" dir="auto">"Monitor"</span>
# </div>
#%% all items in one category "monitor"
category_computers = ['Monitor'] #'laptop', 'mouse', 'keyboard' 

for item in category_computers:

    f = open('search_urls_com_' + item + '.txt', 'w+')
    for i in range(1,251):
        page_url = 'https://www.amazon.com/s?k=' + item + '&i=computers&page=' + str(i) + '&language=en&ref=sr_pg_' + str(i)
        f.write(page_url)
        f.write('\n')
    f.close()

#%% all items in one category "monitor" under "computer accesary"
category_computers = ['monitor'] #'laptop', 'mouse', 'keyboard' 

for item in category_computers:

    f = open('search_urls_com_3_' + item + '.txt', 'w+')
    for i in range(1,251):
        page_url = 'https://www.amazon.com/s?k=' + item + '&i=computers&rh=n%3A1292115011&page=' + str(i) + '&ref=sr_pg_' + str(i)
        f.write(page_url)
        f.write('\n')
    f.close()


#%% all items in one category "electronics"
category_electronics = ['Headphones'] #'DSLR+Camera','smartphone'

for item in category_electronics:

    f = open('search_urls_com_' + item + '.txt', 'w+')
    for i in range(1,251):
        page_url = 'https://www.amazon.com/s?k=' + item + '&i=electronics&page=' + str(i) + '&language=en&ref=sr_pg_' + str(i)
        f.write(page_url)
        f.write('\n')
    f.close()

#%% for multiple categories
category_computers = ['Monitor'] #'laptop', 'mouse', 'keyboard' 
category_electronics = ['Headphones'] #'DSLR+Camera','smartphone'
products = {'computer':'Monitor', 'electronics':'Headphones'}

for category,item in products:

    f = open('search_urls_com_' + item + '.txt', 'w+')
    for i in range(1,10):
        page_url = 'https://www.amazon.com/s?k=' + item + '&i=' + category + '&page=' + str(i) + '&language=en&ref=sr_pg_' + str(i)
        f.write(page_url)
        f.write('\n')
    f.close()

#%%
# output_path = './python/module2/ecommerce/pipe/'
# base_url = 'https://www.amazon.de/s?k=Monitor&ref=nb_sb_noss'
