
import pandas as pd, numpy as np, os
from IPython.display import *
from ipywidgets import *

base = "../data/pizza/"
menus = {}
for s in os.listdir(base):
    df = pd.read_csv(base + s, index_col=0).dropna(axis = 0, subset = ["price"])
    menus[s[:-4]] = df.fillna("N/A").sort_values("price", ascending = False).reset_index(drop = True)

def show_menus():
    @interact(name = Dropdown(options = list(menus.keys()), value = "dominos"))
    def helper(name):
        return menus[name]
    
restraunt = Dropdown(options = list(menus.keys()), value = "dominos")

def pick_data():
    return menus[restraunt.value]