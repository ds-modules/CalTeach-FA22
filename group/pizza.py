
import pandas as pd, numpy as np, os
import plotly.express as px
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

def printmd(s):
    display(Markdown(s))

def plot_party(pizza_price = 14, drink_price = 2.69, slices = 10, cups = 10):
    printmd("## Please Allow 30-45 Seconds for the Plot to Load")
    printmd("### Once the plot loads, use your mouse to drag the plot around and adjust the view!")
    people, budget = 500, 3000
    df = pd.DataFrame(columns = ['Pizza', 'Drink', 'Cost'])
    min_pizza, min_drink = people//slices, people//cups
    for i in list(range(min_pizza, 201)):
        for j in list(range(min_drink, 201)):
            if (cost := i*pizza_price + j*drink_price) <= budget:
                df = df.append({'Pizza': i, 'Drink': j, 'Cost': cost}, ignore_index = True)
    fig = px.scatter_3d(df, x = 'Pizza', y = 'Drink', z = 'Cost', color = 'Cost', opacity = 0.5, template = "seaborn")
    fig = fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), scene_camera = dict(eye=dict(x=1, y=2.5, z=0.1)))
    return fig