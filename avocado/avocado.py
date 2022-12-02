import pandas as pd
import numpy as np
from IPython import *
from IPython.display import *
from scipy.stats import *
import seaborn as sns
import matplotlib.pyplot as plt

haas_prices_2019 = pd.read_csv('https://github.com/ds-modules/CalTeach-FA22/raw/main/data/avocado-19.csv')
haas_prices_2022 = pd.read_csv('https://github.com/ds-modules/CalTeach-FA22/raw/main/data/avocado-19.csv')
samp_2019 = haas_prices_2019.sample(n=50, random_state = 42)
samp_2022 = haas_prices_2022.sample(n=50, random_state = 42)

def printmd(*strings):
    for string in strings:
        display(Markdown(string))


def make_scatter():
    scatter_19 = sns.scatterplot(x = 'ASP Current Year', y = 'Total Bulk and Bags Units', data = samp_2019, color = "#003262", label = "2019")
    scatter_22 = sns.scatterplot(x = 'ASP Current Year', y = 'Total Bulk and Bags Units', data = samp_2022, color = "#FFB300", label = "2022")
    scatter_19.set(xlabel = "Average Price", ylabel = "Total Units Sold")
    scatter_22.set(xlabel = "Average Price", ylabel = "Total Units Sold")
    return scatter_19, scatter_22

def plot_normal():
    fig, ax = plt.subplots()
    plt.style.use('fivethirtyeight')
    x = np.arange(-3.5, 3.5, 0.001)
    y = norm.pdf(x)
    ax.plot(x, y, linewidth=3)
    ax.set_ylim(0, 0.45)
    plt.axvline(x=0, linewidth=2, color="black")
    plt.axhline(y=0, linewidth=6, color="black")
    ax.set_title('Standard Normal Curve')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    plt.show()
    
def plot_t(t = 1):
    fig, ax = plt.subplots()
    plt.style.use('fivethirtyeight')
    x = np.arange(-3.5, 3.5, 0.001)
    y = norm.pdf(x)
    ax.plot(x, y, linewidth=3)
    if t == 1:
        ax.fill_between(x, y, 0, where = (x >= -1) & (x <= 1), alpha=0.3, color='g')
        ax.fill_between(x, y, 0, where = (x <= -1), alpha=0.1, color='r')
        ax.fill_between(x, y, 0, where = (x >= 1), alpha=0.1, color='r')
    else:
        ax.fill_between(x, y, 0, where = (x <= t), alpha=0.3, color='g')
        ax.fill_between(x, y, 0, where = (x >= t), alpha=0.1, color='r')
    ax.set_ylim(0, 0.45)
    plt.axvline(x=0, linewidth=2, color="black")
    plt.axhline(y=0, linewidth=6, color="black")
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    plt.show()
    
def show_stats():
    m_19, s_19 = np.round(norm.fit(samp_2019['ASP Current Year']), 3)
    m_22, s_22 = np.round(norm.fit(samp_2022['ASP Current Year']), 3)
    n_19, n_22 = 50, 50
    printmd("## 2019")
    printmd(r"$\bar{x}_{2019}$:", f"${m_19}$")
    printmd(r"$S_{2019}$:", f"${s_19}$")
    printmd(r"$n_{2019}$:", f"${n_19}$")
    printmd("## 2022")
    printmd(r"$\bar{x}_{2022}$:", f"${m_22}$")
    printmd(r"$S_{2022}$:", f"${s_22}$")
    printmd(r"$n_{2022}$:", f"${n_22}$")
    
def t_test(var):
    t, p = np.round(ttest_ind(samp_2019['ASP Current Year'], samp_2022['ASP Current Year']), 3)
    if var == "t":
        printmd("## T-Test")
        printmd(r"$t$:", f"${t}$")
    elif var == "p":
        printmd("## P-Value")
        printmd(r"$p$:", f"${p}$")
    return t, p
