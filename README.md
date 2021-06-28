# Identifying Drivers for Errors in Zillow's Zestimates

## Executive Summary
The goal of this analysis is to acquire Zillow data regarding single unit properties from 2017, cleaning and analyzing it to create supervised Machine Learning models. These models were used to find drivers of errors in the Zestimate and the sales price of those properties. Unsupervised Machine Learning Techniques like Clustering were then utilized to boost model performance in predicting log errors.

## Key Takeaways
- The square footage, tax values, county and types 1 and 2 of cluster 3 were found to be the best drivers of log error.
- Most variables like number of bedrooms and bathrooms were highly correlated with each other and had low correlation with that target.
- There were many outliers especially in the tax variables indicating some premium properties were part of the dataset.
  - These outliers were removed from the dataset to achieve more normal distributions for our analysis and help train the models better.
- A Standard Scaler was applied to the X variables in the train, validate and test splits.
- The baseline median's RMSE of 0.158350 was utilized as the RMSE to beat
- All models beat this RMSE by a small margin
- The Root Mean Squared Error (RMSE) and R squared were utilized as metrics to evaluate each model's performance
  - RMSE was utilized since we are comparing different size datasets
  - R squared was utilized to evaluate the variance in the model explained by our models
- My best model used OLS Linear Regression and had RMSE of 0.157616 and R squared of 0.003644 on the validate splits. While this beat the median baseline, the R-squared value is very low.
- The model's performance decreased slightly on out of sample data to an RMSE of 0.162519 and R squared of 0.000142 on the test split

## Project Goals
Create scripts to perform the following:
 - acquisition of the dataset
    - Collect data from the codeup database 
 - preparation of the dataset
    - Analyze data and set types appropriately
    - Investigate and handle missing values
    - Consider outliers and other data points of interest
 - exploration of the dataset
    - Examine interactions between independent variables and the target variable using various visualization techniques and analysis
   - Perform clustering to further explore the data. 
 - modeling of the dataset
   - generate at least 4 different models and analyse their performance

## Business Goals
* Find drivers of errors in Zillow's Zestimates
* Attempt to produce a model which will closely replicate (or improve upon) the accuracy of the Zestimate system
   * Note that we are examining the log error present in the Zestimates; logerror is calculated as follows according to Zillow:
   
                                *logerror = log(Zestimate) - log(SalePrice)*

## Project Overview
- The tasks for my project were outlined using this [Trello board](https://trello.com/b/eKZcBkR5/clustering-project).
- Python scripts were used to automate the process of acquiring, preparing and exploring the data
- The data was cleaned by replacing null values, dropping duplicate rows and columns, encoding new features, one hot encoding features.
  - These steps were taken to create the best performing model
- Outliers in the data beyond 1.5 IQR were removed from the dataset
  - We removed outliers from the entire dataset, and not just the train split to improve the model's performance.
- Statistical analyses tested the following hypotheses:
  - Is Log Error significantly different across different size properties?
  - Is Log Error significantly different across different counties?
  - Is Log Error significantly different for homes with more than 6 bathrooms?
  - Is Log Error significantly different for homes with more than 5 bedrooms?
- The data was split into train, test and split dataframes before modeling to avoid data leakage and maintain data integrity
- The elbow method was utilized to find the optimum number of clusters (k) to create for each set of features.
- The following clusters were created:
  - Cluster 1: bathroomcnt, bedroomcnt, calculatedfinishedsquarefeet, age_of_home, buildingqualitytypeid
  - Cluster 2: structuretaxvaluedollarcnt, taxvaluedollarcnt, landtaxvaluedollarcnt, taxamount
  - Cluster 3: bathroomcnt, taxvaluedollarcnt, calculatedfinishedsquarefeet
- Recursive feature enlimination was utilized to select the top 7 features to be included in the models used to predict log error.
- Since our target variable, Log Error, is continuous, we used the following regression algorithms to create models with the intention of beating the baseline:
  - OLS Regression
  - Lasso + Lars
  - Tweedie Regressor GLM
  - Polynomial Regression
- For the purposes of this analysis, we assumed all conditions of Linear Regression were met.
- The best model was fitted on the test data to predict log error

## Initial Hypotheses
*Hypotheses 1:* I rejected the null hypotheses.
* Confidence level = 0.95
* Alpha = 1 - Confidence level = 0.05
* H<sub>0</sub>: Mean logerror for homes with 2064 sqft or less is equivalent to those with more than 2064 sq ft
* H<sub>1</sub>: Mean logerror for homes with 2064 sqft or less is greater than those with more than 2064 sq ft

*Hypotheses 2:* I rejected the null hypotheses.
* Confidence level = 0.95
* Alpha = 1 - Confidence level = 0.05
* H<sub>0</sub>: Mean logerror in Los Angeles County is equivalent to Mean logerror of other counties
* H<sub>1</sub>: Mean logerror in Los Angeles County is not equivalent to Mean logerror of other counties

*Hypotheses 3:* I failed to reject the null hypotheses.
* Confidence level = 0.95
* Alpha = 1 - Confidence level = 0.05
* H<sub>0</sub>: Mean logerror in Orange County is equivalent to Mean logerror of Ventura county
* H<sub>1</sub>: Mean logerror in Orange County is not equivalent to Mean logerror of Ventura county

*Hypotheses 4:* I rejected the null hypotheses.
* Confidence level = 0.95
* Alpha = 1 - Confidence level = 0.05
* H<sub>0</sub>: Mean logerror for properties with more than 3 bathrooms is equivalent to those with 3 or less bathrooms
* H<sub>1</sub>: Mean logerror for properties with more than 3 bathrooms is not equal to those with 3 or less bathrooms

*Hypotheses 5:* I rejected the null hypotheses.
* Confidence level = 0.95
* Alpha = 1 - Confidence level = 0.05
* H<sub>0</sub>: Mean logerror for properties with more than 5 bedrooms is equivalent to those with 5 or less bedrooms
* H<sub>1</sub>: Mean logerror for properties with more than 5 bedrooms is not equivalent to those with 5 or less bedrooms

Data Dictionary

The data was initially comprised of the following columns:
Name | Datatype | Definition | Possible Values
--- | --- | --- | ---
 typeconstructiontypeid | float64 | contruction type| Numeric Value
 storytypeid | float64 | type of story | Numeric Value
 propertylandusetypeid | float64 | property land use type | Numeric Value
 heatingorsystemtypeid | float64 | heating system type | Numeric Value
 buildingclasstypeid | object | building class type | String value
 architecturalstyletypeid| float64 | architectural style | Numeric value
 airconditioningtypeid | float64 | air conditioning type | Numeric value
 parcelid | int64 | unique identifier for each property | Numeric value
 id | int64 | id for each property | Numeric value
 logerror | float64 | log error | Numeric value
 transactiondate | object | transaction date | Date value
 id | int64  | id for this property | Numeric value
 basementsqft | float64 | square foot of basement | Numeric value
 bathroomcnt | float64 | number of bathrooms | Numeric value
 bedroomcnt | float64 | number of bedrooms | Numeric value
 buildingqualitytypeid | float64 | building quality type | Numeric value
 calculatedbathnbr | float64 | calculated number of bathrooms | Numeric value
 decktypeid | float64 | type of deck | Numeric value
 finishedfloor1squarefeet | float64 | square feet of the finished level| Numeric value
 calculatedfinishedsquarefeet | float64 | calculated finished square foot value | Numeric value
 finishedsquarefeet12 | float64 | Square footage | Numeric value
 finishedsquarefeet13 | float64 | Square footage | Numeric value
 finishedsquarefeet15 | float64 | Square footage | Numeric value
 finishedsquarefeet50 | float64 | Square footage | Numeric value
 finishedsquarefeet6 | float64 | Square footage | Numeric value
 fips | float64 | County | 	6037, 6059 or 6111
 fireplacecnt | float64 | Number of fireplaces | Numeric value
 fullbathcnt | float64 | Number of full bathrooms | Numeric value
 garagecarcnt | float64 | Number of cars which fit in the garage | Numeric value
 garagetotalsqft | float64 | Square footage of garage | Numeric value
 hashottuborspa | float64 | Whether the home has a hot tub or spa | Numeric value
 latitude | float64 | Angular distance north/south of the equator, for locating a property | Numeric value
 longitude | float64| Angular distance east/west of the meridian, for locating a property | Numeric value
 lotsizesquarefeet | float64 | Square footage | Numeric value
 poolcnt | float64 | Number of pools | Numeric value
 poolsizesum |  float64 | Size of the pool | Numeric value
 pooltypeid10 |  float64 | Type of Pool | Numeric value
 pooltypeid2 | float64 | Type of Pool | Numeric value
 pooltypeid7 | float64 | Type of Pool | Numeric value
 propertycountylandusecode | object | Property County Land Use | Numeric value
 propertyzoningdesc | object | Property Zone | Numeric value
 rawcensustractandblock | float64 | Census data | Numeric value
 regionidcity | float64 | City | Numeric value
 regionidcounty | float64 | County | Numeric value
 regionidneighborhood | float64 | Neighborhood | Numeric value
 regionidzip | float64 | Zip Code| Numeric value
 roomcnt | float64 | Number of Rooms | Numeric value
 threequarterbathnbr | float64 |  Number of 3/4 Baths| Numeric value
 unitcnt | float64 | Number of Units | Numeric value
 yardbuildingsqft17 | float64 | Square Footage of Yard | Numeric value
 yardbuildingsqft26 | float64 | Square Footage of Yard | Numeric value
 yearbuilt | float64 | Year Built | 4-digit Numeric value
 numberofstories | float64 | Number of Stories | Numeric value
 fireplaceflag | float64 | Fire place configuration | Numeric value
 structuretaxvaluedollarcnt| float64 | Tax Value in Dollars of the structure | Numeric value
 taxvaluedollarcnt | float64 | Tax Value in Dollars | Numeric value
 assessmentyear | float64 | Year of Tax Assessment | Numeric value
 landtaxvaluedollarcnt | float64 | Land Tax Value in Dollars| Numeric value
 taxamount | float64 | Tax Amount | Numeric value
 taxdelinquencyflag | object | Whether or not the Tax is delinquent | String value
 taxdelinquencyyear | float64 | Year the taxes were deemed delinquent | 4-digit Numeric value; NaN if not specified
 censustractandblock | float64 | Census information | Numeric value
 airconditioningdesc | object | Air Conditioning type | String value
 architecturalstyledesc |  object | Architectural Style | String value
 buildingclassdesc |  object | Building Class | String value
 heatingorsystemdesc | object | Heating system type | String value
 propertylandusedesc | object | Property Land Use type| Single Family Residential, Condominium, Cluster Home, Manufactured, Modular, Prefabricated Homes, Mobile Home, Townhouse
 storydesc |  object | Story description type | String value
 typeconstructiondesc | object | Contruction type | String value
 
In addition, during data processing/analysis, the following features were added:
Name | Datatype | Definition | Possible Values 
--- | --- | --- | --- 
age_of_home | integer | currentYear - yearbuilt | Numeric value, basically 2021 - year built

## Project Planning

The overall process followed in this project, is as follows:

- Plan
- Acquire
- Prepare
- Explore 
- Model
- Deliver

### 1. Plan
* Use the <a href="https://trello.com/b/eKZcBkR5/clustering-project">Trello board</a> to compile and track the tasks involved in this project
* Collect required data-source information (namely the database connection details/credentials)
* Perform surface-level examination of the 2017 data

### 2. Acquire
* Acquires the dataset under analysis, using python code within the "acquire.py" script. Uses stored credentials (via env.py) to collect data from the codeup database
* Data is collected from the following tables using a SQL query:
  1. properties_2017
  2. airconditioningtype 
  3. architecturalstyletype 
  4. buildingclasstype 
  5. heatingorsystemtype 
  6. propertylandusetype 
  7. storytype 
  8. typeconstructiontype
  * as was the case in the previous Zillow project, we are focusing on single-unit properties. By definition, this includes any property that matches the following description: "a housing unit within a larger structure that can be used by an individual or household to eat, sleep, and live. The unit can be in any type of residence, such as a house, apartment, or mobile home, and may also be a single unit in a group of rooms"
  * to improve performance, caching was used - the data collected by the aforementioned query was stored in a CSV file on my machine. This allows us to avoid repeated calls to the database by instead using the local copy on subsequent data acquisition calls
  * Finally, this file contains functions to perform and display summarized statistics of the dataframe, and value counts 

### 3. Prepare
* This step involves the cleaning and preparation of the data. To increase modularity, this functionality is a part of the "prepare.py" python script.
* The script performs a number of functions, such as:
  * drops rows and columns with missing values above a specified threshold
  * dropping duplicate columns and rows
  * removes properties which meet the following criteria:
    * contains 0 beds AND 0 baths - these appear to be erroneous data
    * lists square footage as "0"
  * replace missing values in the yearbuilt column, with the median
  * encode the age of home as currentYear - age_of_home, to give it a relative value
  * encode the fips column to produce three regions: LA_county, orange_county and ventura_county
  * split the data into train/test/validate splits
  * Removed outliers beyond 1.5 IQR were removed
  * during this phase, we also imputed several values using the median and mostFrequent strategies, as applicable

### 4. Explore
 * Perform bivariate analysis, by generating bar plots for categorical variables, as well as scatter plots for continuous variables
 * Performs multivariate analysis by generating scatter plots of each continuous variable against the target variable, by each categorical variable
 * Use tools such as a heatmap to discover correlation between features and the target variable
 * Use pairplots to analyze interactions between variables; these will help find distinct clusters where relationships are not driven solely by linear correlation
 * Use a scalar to ensure that the data is scaled 
 * Use the above information to generate three different clusters:
   1. Cluster1: bathroomcnt, bedroomcnt, calculatedfinishedsquarefeet, age_of_home, buildingqualitytypeid
   2. Cluster2: structuretaxvaluedollarcnt, taxvaluedollarcnt, landtaxvaluedollarcnt, taxamount 
   3. Cluster3: bathroomcnt, taxvaluedollarcnt, calculatedfinishedsquarefeet 
 * Performed means testing on the clusters and decided to use only cluster #3 above in models
 * One-hot encoded Cluster3 to create a new feature for each set in the cluster

### 5. Model
 * Use the median log error to establish a baseline
 * make use of the following regression algorithms to generate models:
    1. OLS Regression
    2. Lasso + Lars
    3. Tweedie Regressor GLM
    4. Polynomial Regression
 * evaluate the RMSE and R-Squared and compare the output of each model to the baseline and against other models
 * Fit the best model on the test-data split

### 6. Deliver
Present findings via Jupyter Notebook

## Reproducing the Project
Simply clone the project locally and create an env.py file in the same folder as the cloned code. The format should be as follows:

```
host = ‘DB_HOST_IP’
user =  ‘USERNAME’
password = ‘PASSWORD’

def get_db_url(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
```
    
In the above code, replace the `host`, `user` and `password` values with the correct Database Host IP address, Username and Password.

Next, open the [Jupyter notebook](https://github.com/mariamnaqvi/predicting-log-error/blob/main/final_report_clustering.ipynb) and execute the code within. 

## Conclusion & Next Steps
- The best drivers of log error were found to be the tax variables, location in LA county and sets of cluster 3 which contains bathroomcnt, taxvaluedollarcnt and calculatedfinishedsquarefeet
- The best performing model is the OLS Linear Regression Model.
- If I had more time, I would explore the creation of more clusters and possibly collect more data especially on premium propeties so as much information is not lost to outliers.

