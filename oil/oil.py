import pandas as pd
import numpy as np
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
    oil["barrels"] = 1000 * oil["barrels"]
    return oil

oil = load_oil()
    
def plot_oil():
    printmd('<p style="font-size:20px"> Use the dropdown below to select <code>scatter</code> or <code>line</code> to show a scatter plot, or a line plot, respectively! </p>')
    @interact(graph = Dropdown(options = ["scatter", "line"], value = "scatter"))
    def plot(graph):
        f = px.scatter
        if graph == "line":
            f = px.line
        return f(oil, x = "date", y = "barrels", template = "seaborn", title = "Oil Production in the United States")
    
def oil_line():
    printmd("<p style = 'font-size: 20px'> Use the checkbox below to show the linear regression line in the plot!</p>")
    @interact(line = Checkbox(value = False, description = "Show regression line"))
    def helper(line):
        if line:
            fig =  px.scatter(oil, x = "date", y = "barrels", template = "seaborn", title = "Oil Production in the United States", trendline = "ols")
        else:
            fig = px.scatter(oil, x = "date", y = "barrels", template = "seaborn", title = "Oil Production in the United States")
        return fig
        
def show_history():
    return IFrame("https://www.historycentral.com/Today/21st.html#:~:text=2003%2D%20U.S.%20Invades%20Iraq", width = "100%", height = 600)

def r_scatter(r = None, num = 10):
    "Generate a scatter plot with a correlation approximately r"
    if r:
        x = np.random.normal(0, 1, num)
        z = np.random.normal(0, 1, num)
        y = r*x + (np.sqrt(1-r**2))*z
        fig = px.scatter(x = x, y = y, template = "seaborn")
        fig.update_layout(height = 600, width = 600)
        fig.show()
    else:
        printmd("<p style = 'font-size: 20px'> Use the slider below to change the correlation between the two variables!</p>")
        printmd("<p style = 'font-size: 20px'> Use the dropdown to select how many points to plot!</p>")
        printmd("<p style = 'font-size: 20px'> Use the checkbox to show the linear regression line!</p>")
        @interact(r = FloatSlider(min = -1, max = 1, value = .2, step= .05), n = Dropdown(options = [10, 100, 1000], value = 100), line = Checkbox(value = False, description = "Show regression line"))
        def helper(r, n = 100, line = False):
            x = np.random.normal(0, 1, n)
            z = np.random.normal(0, 1, n)
            y = r*x + (np.sqrt(1-r**2))*z
            if line:
                fig = px.scatter(x = x, y = y, template = "seaborn", title = f"Scatter of variables with correlation r={r}", trendline = "ols")
            else:
                fig = px.scatter(x = x, y = y, template = "seaborn", title = f"Scatter of variables with correlation r={r}")
            fig.update_layout(height = 600, width = 600)
            fig.show()
            
def corr_examples(r, line = False):
    x = np.random.normal(0, 1, 50)
    z = np.random.normal(0, 1, 50)
    y1 = r*x + (np.sqrt(1-r**2))*z
    y2 = (-r)*x + (np.sqrt(1-(-r)**2))*z
    df1 = pd.DataFrame({"x": x, "y": y1, "label" : ["test 1"]*50})
    df2 = pd.DataFrame({"x": x, "y": y2, "label" : ["test 2"]*50})
    df = pd.concat([df1, df2])
    if line:
        fig = px.scatter(df, x = "x", y = "y", template = "seaborn", facet_col = "label", trendline = "ols")
    else:
        fig = px.scatter(df, x = "x", y = "y", template = "seaborn", facet_col = "label")
    fig.update_layout(height = 400, width = 800)
    fig.show()