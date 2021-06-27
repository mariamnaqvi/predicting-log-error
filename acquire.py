import pandas as pd
import numpy as np
import os
# use get_db_url function to connect to the codeup db
from env import get_db_url


def get_zillow_data(cached=False):
    '''
    This function returns the zillow database as a pandas dataframe. 
    If the data is cached or the file exists in the directory, the function will read the data into a df and return it. 
    Otherwise, the function will read the database into a dataframe, cache it as a csv file
    and return the dataframe.
    '''
    # If the cached parameter is false, or the csv file is not on disk, read from the database into a dataframe
    if cached == False or os.path.isfile('zillow_df.csv') == False:
        sql_query = '''
        SELECT * 
        FROM predictions_2017 pred
        LEFT JOIN properties_2017 USING(parcelid)
        LEFT JOIN airconditioningtype USING(airconditioningtypeid)
        LEFT JOIN architecturalstyletype USING(architecturalstyletypeid)
        LEFT JOIN buildingclasstype USING(buildingclasstypeid)
        LEFT JOIN heatingorsystemtype USING(heatingorsystemtypeid)
        LEFT JOIN propertylandusetype USING(propertylandusetypeid)
        LEFT JOIN storytype USING(storytypeid)
        LEFT JOIN typeconstructiontype USING(typeconstructiontypeid)
        WHERE pred.transactiondate LIKE '2017%'
        AND latitude IS NOT NULL
        AND longitude IS NOT NULL
        AND propertylandusetypeid IN (261, 263, 264, 265, 266, 268, 273, 275, 276, 279);  
        '''
        zillow_df = pd.read_sql(sql_query, get_db_url('zillow'))
        #also cache the data we read from the db, to a file on disk
        zillow_df.to_csv('zillow_df.csv')
    else:
        # either the cached parameter was true, or a file exists on disk. Read that into a df instead of going to the database
        zillow_df = pd.read_csv('zillow_df.csv', index_col=0)
    # return our dataframe regardless of its origin
    return zillow_df


def summarize(df):
    '''
    This function will take in a single argument (a pandas dataframe) and 
    output to console various statistices on said dataframe, including:
    # .shape
    # .info()
    # value_counts()
    # observation of nulls in the dataframe
    '''
    # Print out the "shape" of our dataframe - the rows and columns we have to work with
    print(f'The zillow dataframe has {df.shape[0]} rows and {df.shape[1]} columns.')
    print('')
    print('-------------------')

    # print the number of missing values in our dataframe
    print(f'There are total of {df.isna().sum().sum()} missing values in the entire dataframe.')
    print('')
    print('-------------------')

    # print information regarding column datatypes and non null counts
    df.info()
    print('')
    print('-------------------')

    print('Here are the categories and their relative proportions')
    # check different categories and proportions of each category for object type cols
    show_vc = ['fips','bathroomcnt','bedroomcnt', 'propertylandusedesc', 'buildingqualitytypeid']
    for col in df.columns:
        if col in show_vc:
            print(f'value counts of {col}')
            print(df[col].value_counts())
            print('')
            print(f'proportions of {col}')
            print(df[col].value_counts(normalize=True,dropna=False))
            print('-------------------')
    
    
    
    


