import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def box_plot(data, column1, column2, title, hue):

    if hue[0]==0:

        sns.boxplot(data=data,x=column1,y=column2)
        plt.title(title)


    else:

        sns.boxplot(data=data,x=column1,y=column2, hue=hue[1])
        plt.title(title)


import scipy.stats as stats

def check_normal(data):
    
    _ = stats.probplot(data, plot=plt)

        
    _, pVal = stats.shapiro(data)

    if pVal > 0.05:
        
        print(f'Shapiro P-value: {pVal} ')
        
    else:
        
        print(f'Shapiro P-value: {pVal} ')

