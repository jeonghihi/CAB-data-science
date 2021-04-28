#%%
import os
import shutil

#%% all filenames within source_dir (all children dir)
source_dir = r'C:\Users\Jeong'
filenames_list = []

for root, dirs, filenames in os.walk(source_dir):
     for filename in filenames:
        filenames_list.append(filename)

filenames_list

#%% all filenames at source_dir

source_dir = r'C:\Users\Jeong'
filenames_list = []

for filenames in os.walk(source_dir):
     for filename in filenames:
        filenames_list.append(filename)

filenames_list
# %%
import pandas as pd 

output_path = r''

df = pd.DataFrame(filenames_list)
df.to_csv(output_path+'\filenames.csv')