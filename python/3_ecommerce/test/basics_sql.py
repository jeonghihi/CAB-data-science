# settings
import numpy as np 
import pandas as pd 
import json
from sqlalchemy import create_engine
import pymysql  
import mysql.connector

#%% login/connection settings for mysql
passwrd = 'hellomysql!'
db_name = 'ecom'
db_data = 'mysql+mysqldb://' + 'root' + ':' + passwrd + '@' + 'localhost' + ':3306/' \
       + db_name + '?charset=utf8mb4'

engine = create_engine(db_data)

# Connect to the database
connection = pymysql.connect(host='localhost',
                         user='root',
                         password=passwrd,
                         db='ecom')
# create cursor
cursor=connection.cursor()

#%% query : SHOW X FROM X

query = "SHOW tables FROM ecom"

df = pd.read_sql(query, con=connection)
print(df)

#%% query : groupby
query = "SELECT country,  FROM sales"
df = pd.read_sql(query, con=connection)
print(df)

#%% query : window 3


#%% end

engine.dispose()
connection.close()