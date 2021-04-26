# pip install PyMySQL
# pip install SQLAlchemy==1.4.8
# pip install mysql-connector-python
# pip install cryptography

#%% 
# settings
import numpy as np 
import pandas as pd 
import json
from sqlalchemy import create_engine
import pymysql  

#%% import csv to sql database (by Shekhar) 

# load dataset
item = 'headphones'
#item = 'monitor'
s = pd.read_csv('./data/ecom-web/' + item + '_summary.csv')
p = pd.read_csv('./data/ecom-web/' + item + '_details.csv')

# my_file = pd.read_csv('./data/ecom-sales/sales_summary.csv')
# my_file.to_sql('sales_summary', engine, if_exists='append', index=False)  

s.head()

#%% login setting for sql
passwrd = 'hellomysql!'
db_name = 'ecom'
db_data = 'mysql+mysqldb://' + 'root' + ':' + passwrd + '@' + 'localhost' + ':3306/' \
       + db_name + '?charset=utf8mb4'

engine = create_engine(db_data)
    # when error (No module named 'MySQLdb') occurs:
    # solution: https://stackoverflow.com/questions/53024891/modulenotfounderror-no-module-named-mysqldb
    # install mysql-connector-python

# Connect to the database
connection = pymysql.connect(host='localhost',
                         user='root',
                         password=passwrd,
                         db='ecom')

# create cursor
cursor=connection.cursor()

#%%
# Execute the to_sql for writting DF into SQL
s.to_sql('headphones_s', engine, if_exists='append', index=False)    
p.to_sql('headphones_p', engine, if_exists='append', index=False)   

# load more datasets
dslr = pd.read_csv('./data/ecom-sales/dslr.csv')
keyboard = pd.read_csv('./data/ecom-sales/keyboard.csv')
monitor = pd.read_csv('./data/ecom-sales/monitor.csv')
mouse = pd.read_csv('./data/ecom-sales/mouse.csv') 
processor = pd.read_csv('./data/ecom-sales/processor.csv')
sales = pd.read_csv('./data/ecom-sales/sales.csv') 
smartphone = pd.read_csv('./data/ecom-sales/smartphone.csv')
product_summary = pd.read_csv('./data/ecom-web/product_summary.csv')

# import these to sql
dslr.to_sql('dslr_sales', engine, if_exists='append', index=False)   
keyboard.to_sql('keyboard_sales', engine, if_exists='append', index=False)   
monitor.to_sql('monitor_sales', engine, if_exists='append', index=False)   
mouse.to_sql('mouse_sales', engine, if_exists='append', index=False)   
processor.to_sql('processor_sales', engine, if_exists='append', index=False)   
sales.to_sql('sales', engine, if_exists='append', index=False)   
smartphone.to_sql('smartphone_sales', engine, if_exists='append', index=False)   
product_summary.to_sql('product_summary', engine, if_exists='append', index=False)   


engine.dispose()
connection.close()

# %% create database in sql

sqlEngine = create_engine('mysql+pymysql://root:Host!98342@127.0.0.1/amazon', pool_recycle=3600)

dbConnection = sqlEngine.connect()

# This is for creating data base
sqlEngine.execute("CREATE DATABASE IF NOT EXISTS AMAZON") #create db
sqlEngine.execute("USE AMAZON") # select new db

tableName   = "summary"


try:
    frame = s.to_sql(tableName, dbConnection, if_exists='replace',index = False)

except ValueError as vx:
    print(vx)

except Exception as ex:   
    print(ex)

else:
    print("Table %s created successfully."%tableName)

finally:
    dbConnection.close()
