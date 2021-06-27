import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats as stats
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

def generate_barplot(df, target, var):
    '''
    Helper function to generate barplots. Given a dataframe df, a target column and a 
    variable, this will generate and draw a barplot for that variable.
    '''
    overall_mean = df[target].mean()
    sns.barplot(var, target, data=df, palette="twilight_shifted")
    plt.xlabel('')
    plt.ylabel('Log Error')
    plt.title('Bar plot of ' + var + ' vs ' + target)
    plt.axhline(overall_mean, ls = '--', color = 'grey')
    plt.show()


def generate_scatterplot(df, target, var):
    '''
    This function takes in a dataframe, the target variable and the independent variable which are both continuous. 
    It creates a scatter plot with the predictor as the x variable and the target as the y variable.
    '''
    sns.relplot(x=var, y=target, data=df)


def explore_bivariate(df, target, cat_vars, cont_vars):
    '''
    This function takes in takes in a dataframe, the name of the target variable, a list of 
    the names of the categorical variables and a list of the names of the continuous variables. It returns
    bar plots for categorical variables and scatterplots for continuous variables.
    For each categorical variable, the bar plot shows the log error for each class in each category
    with a dotted line for the average overall log error. 
    The scatterplots show the relationship between continuous independent variables and the target variable.
    '''
    for var in cat_vars:
        # bar plot with overall horizontal line
        generate_barplot(df, target, var)
    for var in cont_vars:
        # creates scatterplot
        generate_scatterplot(df, target, var)


def explore_multivariate(train, target, cat_vars, cont_vars):
    '''
    This function takes in takes in a dataframe, the name of the target variable, a list of 
    the names of the categorical variables and a list of the names of the continuous variables.
    It generates scatterplots showing the target variable for each class of the categorical variables 
    against the continuous variables.
    '''
    for cat in cat_vars:
        for cont in cont_vars:
            sns.relplot(x=cont, y=target, data=train, hue=cat, palette ='twilight_shifted')
            plt.xlabel(cont)
            plt.ylabel(target)
            plt.title(cont + ' vs ' + target + ' by ' + cat)
            plt.show()


def create_heatmap(train, cols):
    '''
    This function takes in the training split as well as the columns to find correlation for. 
    It creates a correlation matrix and then displays a heatmap showing all of the correlations. 
    The highest correlation values have the darkest colors in this heatmap.
    '''
    corr_matrix = train[cols].corr()
    plt.figure(figsize=(15,8))
    sns.heatmap(corr_matrix, cmap='twilight_shifted', annot=True, linewidth=0.5, mask= np.triu(corr_matrix))
    plt.title('Correlation with the target and among features in the train split')
    plt.show()


def correlation_exploration(train, cols, target):
    '''
    This function takes in the train split, a list of predictors, 
    and the target for a y-axis variable in the df and displays a scatter plot, the r-
    squared value, and the p-value. It explores the correlation between the predictors (x 
    variables) and the target (y variable).
    '''
    for var in cols:
        r, p = stats.pearsonr(train[var], train[target])
        df.plot.scatter(var, target)
        plt.title(f"{var}'s Relationship with {target}")
        print(f'The p-value is: {p}. There is {round(p,3)}% chance that we see these results by chance.')
        print(f'r = {round(r, 2)}')
        plt.show()


def plot_variable_pairs(train, cols, hue=None):
    '''
    This function takes in a df, a list of cols to plot, and default hue=None 
    and displays a pairplot with a red regression line.
    '''
    plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.7}}
    sns.pairplot(train[cols], hue=hue, kind="reg",plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.1}})
    plt.show()


def select_rfe(X, y, k, return_rankings=False, model=LinearRegression()):
    '''
    This function takes in the X variables as a dataframe, the target variable, number of features to 
    select for modeling (k) with default modle set to Linear Regression. It returns the top k features 
    as well as the rankings for all features.
    '''
    # Use the passed model, LinearRegression by default
    rfe = RFE(model, n_features_to_select=k)
    rfe.fit(X, y)
    features = X.columns[rfe.support_].tolist()
    if return_rankings:
        rankings = pd.Series(dict(zip(X.columns, rfe.ranking_)))
        return features, rankings
    else:
        return features