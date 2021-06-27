# cleaning the df
import pandas as pd
import numpy as np

# for splitting the df
from sklearn.model_selection import train_test_split

# to convert yearbuilt
from datetime import date

# to impute missing values
from sklearn.impute import SimpleImputer

# to find the difference 
from collections import Counter

# for scaling data
from sklearn.preprocessing import StandardScaler, RobustScaler

def handle_missing_values(df, prop_required_column=0.5 , prop_required_row=0.75):
    '''
    This function takes in a pandas dataframe, default proportion of required columns (set to 50%) and proprtion of required rows (set to 75%).
    It drops any rows or columns that contain null values more than the threshold specified from the original dataframe and returns that dataframe.
    
    Prior to returning that data, it will print statistics and list counts/names of removed columns/row counts 
    '''
    original_cols = df.columns.to_list()
    original_rows = df.shape[0]
    threshold = int(round(prop_required_column * len(df.index), 0))
    df = df.dropna(axis=1, thresh=threshold)
    threshold = int(round(prop_required_row * len(df.columns), 0))
    df = df.dropna(axis=0, thresh=threshold)
    remaining_cols = df.columns.to_list()
    remaining_rows = df.shape[0]
    dropped_col_count = len(original_cols) - len(remaining_cols)
    dropped_cols = list((Counter(original_cols) - Counter(remaining_cols)).elements())
    print(f'The following {dropped_col_count} columns were dropped because they were missing more than {prop_required_column * 100}% of data: \n{dropped_cols}\n')
    dropped_rows = original_rows - remaining_rows
    print(f'{dropped_rows} rows were dropped because they were missing more than {prop_required_row * 100}% of data')
    return df


def prep_zillow(df):
    '''
    This function takes in a pandas dataframe, removes duplicate rows and columns, 
    handles missing values, drops columns with nulls beyond threshold specified, removes properties 
    witn 0 beds and 0 baths as well as any with 0 baths or square footage of 0.
    '''
    
    # drop duplicate columns
    df = df.loc[:,~df.columns.duplicated()]

    # check for duplicates 
    num_dups = df.duplicated().sum()
    # if we found duplicate rows, we will remove them, log accordingly and proceed
    if num_dups > 0:
        print(f'There are {num_dups} duplicate rows in your dataset - these will be dropped.')
        print ('----------------')
        # remove the duplicates found
        df = df.drop_duplicates()

    else:
        # otherwise, we log that there are no dupes, and proceed with our process
        print(f'There are no duplicate rows in your dataset.')
        print('----------------')

    # dropping cols/rows where more than half of the values are null
    df = handle_missing_values(df, prop_required_column = .6, prop_required_row = .75)

    # keep only properties with more than 0 beds and 0 baths
    df = df[(df.bedroomcnt > 0) & (df.bathroomcnt > 0)]
    
    # # remove properties with 0 baths
    df = df[df.bathroomcnt > 0]

    # # keep only properties with square footage greater than 0
    df = df[df.calculatedfinishedsquarefeet > 0]

    # Creating new feature age_of_home
    # find median yearbuilt 
    median_year = df.yearbuilt.median()

    # replace the missing values in the yearbuilt column with the above calculated median value
    df['yearbuilt'] = df['yearbuilt'].replace(np.NaN, median_year)

    # encode yearbuilt as age of home in years as an integer
    df['age_of_home'] = (date.today().year - df.yearbuilt).astype(int)

    #----------------------#
    #  One hot encoding    #
    #----------------------#

    # encode categorical variable: county to numeric
    dummy_df=pd.get_dummies(df['fips'], dummy_na=False, 
                            drop_first=False)

    # rename columns that have been one hot encoded
    dummy_df = dummy_df.rename(columns={6037.0: 'LA_county', 6059.0: 'orange_county', 6111.0: 'ventura_county'})  

    # join dummy df to original df
    df = pd.concat([df, dummy_df], axis=1)

    # return cleaned dataframe
    return df


def split_zillow(df, seed=123):
    '''
    This function takes in a pandas dataframe and a random seed. It splits the original
    data into train, test and split dataframes, prints out their shapes and returns the splits.
    Test dataset is 20% of the original dataset
    Train is 56% (0.7 * 0.8 = .56) of the original dataset
    Validate is 24% (0.3 * 0.7 = 0.24) of the original dataset
    '''
    train, test = train_test_split(df, train_size=0.8, random_state=seed)
    train, validate = train_test_split(train, train_size=0.7, random_state=seed)

    # Now that we have our 3 dataframes, print their shapes and return them    
    
    print(f'Shape of train split: {train.shape}')

    print ('----------------')

    print(f'Shape of test split: {validate.shape}')

    print ('----------------')

    print(f'Shape of validate split: {test.shape}')

    print ('----------------')

    return train, validate, test


def impute(df, my_strategy, column_list):
    ''' 
    This function takes in a df, strategy, and column list and
    returns df with listed columns imputed using the imputing stratagy specififed
    '''
    # build imputer    
    imputer = SimpleImputer(strategy=my_strategy)  
    # fit/transform selected columns
    df[column_list] = imputer.fit_transform(df[column_list]) 

    return df


def scale_data(X_train, X_validate, X_test):
    '''
    This function takes in the features for train, validate and test splits. It creates a Standard Scaler and fits that to the train set.
    It then transforms the validate and test splits and returns the scaled features for the train, validate and test splits.
    '''
    # create scaler
    scaler = StandardScaler()
    # Note that we only call .fit with the training data,
    # but we use .transform to apply the scaling to all the data splits.
    scaler.fit(X_train)

    # convert scaled variables to a dataframe 
    X_train_scaled = pd.DataFrame(scaler.transform(X_train),index=X_train.index,
                                    columns=X_train.columns)
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate), index=X_validate.index,
                                    columns=X_validate.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), index=X_test.index,
                                    columns=X_test.columns)

    return X_train_scaled, X_validate_scaled, X_test_scaled

    
def remove_outliers(df, cols, k):
    '''
    This function checks for outliers in original dataframe and removes all outliers not within IQR. 
    '''
    for col in cols:
        q1, q3 = df[col].quantile([.25, .75])
        iqr = q3 - q1
        upper_bound = q3 + k * iqr
        lower_bound = q1 - k * iqr
        df = df[(df[col] < upper_bound) & (df[col] > lower_bound)]   
    return df