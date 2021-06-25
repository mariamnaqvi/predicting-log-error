import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# custom module imports
import acquire as aq
import prepare as pr

import scipy.stats as stats
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor

def explore_univariate(df, cat_vars, cont_vars):
    '''
    This function takes in categorical and continuous variables as well as a pandas dataframe.
    It returns a bar plot for each categorical variable
    and a histogram and boxplot for each continuous variable.
    '''
    # plot frequencies for each categorical variable
    for var in cat_vars: 
        print('Bar Plot of ' + var)
        bp = df[var].hist()
        plt.xlabel(var)
        plt.ylabel('count')
        bp.grid(False)
        plt.show()
    
    # print histogram for each continuous variable
    for var in cont_vars:
        generate_hist(df, var)
        # creating boxplot for each variable
        plt.figure(figsize=(10,5))
        sns.boxplot(x=var, data=df,  palette="twilight_shifted")
        plt.title('Distribution of ' + var)
        plt.show()

def generate_hist(df, var):
    '''
    Helper function. Given a dataframe df and a variable to plot, this function will 
    generate and display a histogram for that variable.
    '''
    print ('Distribution of ' + var)
    df[var].hist(bins=100)
    plt.grid(False)
    plt.xlabel(var)
    plt.ylabel('Number of Properties')
    plt.show()