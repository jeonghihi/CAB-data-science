#%% for one category
f = open('search_urls.txt', 'w+')

for i in range(1,31):
    page_url = 'https://www.amazon.de/s?k=laptop&page=' + str(i) + '&language=en&ref=sr_pg_' + str(i)
    f.write(page_url)
    f.write('\n')

f.close()

# if products has less than 10 pages, find number of pages of the products
# (div class= "a-section a-spacing-small a-spacing-top-small")
# <div class="a-section a-spacing-small a-spacing-top-small"><span dir="auto">1-16 of over 2,000 results for</span><span dir="auto"> </span><span class="a-color-state a-text-bold" dir="auto">"Monitor"</span>
# </div>

#%% for multiple categories
category = ['DSLR+Camera','smartphone','laptop', 'mouse', 'keyboard','headphones'] 

for item in category:
    f = open('search_urls_' + item + '.txt', 'w+')
    for i in range(1,31):
        page_url = 'https://www.amazon.de/s?k=' + item + '&page=' + str(i) + '&ref=nb_sb_noss&language=en&ref=sr_pg_' + str(i)
        f.write(page_url)
        f.write('\n')
    
    f.close()

#%%
# output_path = './python/module2/ecommerce/pipe/'
# base_url = 'https://www.amazon.de/s?k=Monitor&ref=nb_sb_noss'
