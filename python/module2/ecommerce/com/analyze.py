# %% packages
# ========== packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# %% 
# load dataset
filepath = './output/product_summary.csv'
raw_data = pd.read_csv(filepath, sep=",", engine="python")
raw_data.head()
# %%
