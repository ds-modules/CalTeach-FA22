import pandas as pd
import plotly.express as px
from ipywidgets import *
from IPython import *
from IPython.display import *


def printmd(s):
    display(Markdown(s))


def load_oil():
    oil = pd.read_csv("../data/oil.csv", skiprows = 4, )
    oil["Date"] = pd.to_datetime(oil.Month)
    oil.columns = ["month", "barrels", "date"]
    oil = oil[["month", "date", "barrels"]]
    return oil

def plot_oil():
    oil = load_oil()
    printmd('<p style="font-size:20px"> Use the dropdown below to select <code>scatter</code> or <code>line</code> to show a scatter plot, or a line plot, respectively! </p>')
    @interact(graph = Dropdown(options = ["scatter", "line"], value = "scatter"))
    def plot(graph):
        f = px.scatter
        if graph == "line":
            f = px.line
        return f(oil, x = "date", y = "barrels", template = "seaborn")
        