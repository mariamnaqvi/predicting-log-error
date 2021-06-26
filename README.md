# Clustering Project - Identifying Drivers for Errors in Zillow's Zestimates

## Project Description
Perform further analysis on the Zillow 2017 dataset, performing data cleaning, processing and exploration before using statistical analysis to derive valuable conclusions. Furthermore, create a model which will accurately predict the logerror present in Zillow's Zestimate system, isolating the features ("drivers") used to calculate Zestimate values.

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
   - Perform clustering to further explore the data. Use at 3 combinations of features
 - modeling of the dataset
   - generate at least 4 different models and analyse their performance

## Business Goals
* Find drivers of errors in Zillow's Zestimate system
* Attempt to produce a model which will closely replicate (or improve upon) the accuracy of the Zestimate system
   * Note that we are examining the log error present in the Zestimate system; logerror will be calculated as follows:
   
                                *logerror = log(Zestimate) - log(SalePrice)*

## Initial Hypotheses
*Hypotheses X:* 
* Confidence level = 0.95
* Alpha = 1 - Confidence level = 0.05
* H<sub>0</sub>: Variance in logerror in Los Angeles county and other counties are equivalent
* H<sub>1</sub>: Variance in logerror in Los Angeles county and other counties are not equivalent

*Hypotheses X:* 
* Confidence level = 
* Alpha = 1 - Confidence level = 
* H<sub>0</sub>: Mean logerror in Los Angeles County is equivalent to Mean Error of other counties
* H<sub>1</sub>: Mean logerror in Los Angeles County is not equivalent to Mean Error of other counties

*Hypotheses X:* 
* Confidence level = 0.95
* Alpha = 1 - Confidence level = 0.05 
* H<sub>0</sub>: Variance in logerror in Orange county and Ventura county are equivalent
* H<sub>1</sub>: Variance in logerror in Orange county and Ventura county are not equivalent

*Hypotheses X:* 
* Confidence level = 
* Alpha = 1 - Confidence level = 
* H<sub>0</sub>: Mean logerror in Orange County is equivalent to Mean Error of Ventura county
* H<sub>1</sub>: Mean logerror in Orange County is not equivalent to Mean Error of Ventura county

*Hypotheses X:* 
* Confidence level = 0.95
* Alpha = 1 - Confidence level = 0.05 
* H<sub>0</sub>: Variance in logerror in properties with more than 6 bathrooms and others are equivalent
* H<sub>1</sub>: Variance in logerror in properties with more than 6 bathrooms and others are not equivalent

*Hypotheses X:* 
* Confidence level = 
* Alpha = 1 - Confidence level = 
* H<sub>0</sub>: Mean logerror for properties with more than 6 bathrooms is equivalent to those with 6 or less bathrooms
* H<sub>1</sub>: Mean logerror for properties with more than 6 bathrooms is not equal to those with 6 or less bathrooms


Data Dictionary

The data was initially comprised of the following columns:
Name | Datatype | Definition | Possible Values 
--- | --- | --- | --- 
 typeconstructiontypeid | non-null | float64
 storytypeid | non-null | float64
 propertylandusetypeid | non-null | float64
 heatingorsystemtypeid | non-null | float64
 buildingclasstypeid | non-null | object 
 architecturalstyletypeid | non-null | float64
 airconditioningtypeid | non-null | float64
 parcelid | non-null | int64  
 id | non-null | int64  
 logerror | non-null | float64
 transactiondate | non-null | object 
 id | non-null | int64  
 basementsqft | non-null | float64
 bathroomcnt | non-null | float64
 bedroomcnt | non-null | float64
 buildingqualitytypeid | non-null | float64
 calculatedbathnbr | non-null | float64
 decktypeid | non-null | float64
 finishedfloor1squarefeet | non-null | float64
 calculatedfinishedsquarefeet | non-null | float64
 finishedsquarefeet12 | non-null | float64
 finishedsquarefeet13 | non-null | float64
 finishedsquarefeet15 | non-null | float64
 finishedsquarefeet50 | non-null | float64
 finishedsquarefeet6 | non-null | float64
 fips | non-null | float64
 fireplacecnt | non-null | float64
 fullbathcnt | non-null | float64
 garagecarcnt | non-null | float64
 garagetotalsqft | non-null | float64
 hashottuborspa | non-null | float64
 latitude | non-null | float64
 longitude | non-null | float64
 lotsizesquarefeet | non-null | float64
 poolcnt | non-null | float64
 poolsizesum | non-null | float64
 pooltypeid10 | non-null | float64
 pooltypeid2 | non-null | float64
 pooltypeid7 | non-null | float64
 propertycountylandusecode | non-null | object 
 propertyzoningdesc | non-null | object 
 rawcensustractandblock | non-null | float64
 regionidcity | non-null | float64
 regionidcounty | non-null | float64
 regionidneighborhood | non-null | float64
 regionidzip | non-null | float64
 roomcnt | non-null | float64
 threequarterbathnbr | non-null | float64
 unitcnt | non-null | float64
 yardbuildingsqft17 | non-null | float64
 yardbuildingsqft26 | non-null | float64
 yearbuilt | non-null | float64
 numberofstories | non-null | float64
 fireplaceflag | non-null | float64
 structuretaxvaluedollarcnt | non-null | float64
 taxvaluedollarcnt | non-null | float64
 assessmentyear | non-null | float64
 landtaxvaluedollarcnt | non-null | float64
 taxamount | non-null | float64
 taxdelinquencyflag | non-null | object 
 taxdelinquencyyear | non-null | float64
 censustractandblock | non-null | float64
 airconditioningdesc | non-null | object 
 architecturalstyledesc | non-null | object 
 buildingclassdesc | non-null | object 
 heatingorsystemdesc | non-null | object 
 propertylandusedesc | non-null | object 
 storydesc | non-null | object 
 typeconstructiondesc | non-null | object
 
In addition, during data processing/analysis, the following features were added:
Name | Datatype | Definition | Possible Values 
--- | --- | --- | --- 
parcelid|non-null  int64|Unique identifier for each property|Numeric value

## Project Planning

The overall process followed in this project, is as follows:

Plan
Acquire
Prepare
Explore 
Model
Deliver

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
  * Additionally, latitude and longitude were removed via the sql query; these values contained a number of nulls which did not provide added value for this analysis
  * Finally, this file contains functions to perform summarization and data regarding the number of nulls by column and row 

### 3. Prepare
* This step involves the cleaning and preparation of the data. To increase modularity, this functionality is a part of the "prepare.py" python script.
* The script performs a number of functions, such as:
  * removing duplicate ParcelIds - these represent duplicate records
  * dropping duplucate columns
  * checking for other duplicate records, wherein the entire data record is duplicated (and removing them if found)
  * dropping columns and rows where more than half of the values are null - these are considered unhelpful
  * drop 5 additional columns which clearly contain a large number of nulls:
    * heatingorsystemtypeid
    * buildingqualitytypeid
    * propertyzoningdesc
    * unitcnt
    * heatingorsystemdesc
  * encode the age of home as currentYear - age_of_home, to give it a relative value
  * encode the fips column to produce three regions: LA_county, orange_county and ventura_county
  * 

### 4. Explore
 * Perform bivariate analysis, by generating bar plots for categorical variables, as well as scatter plots for quantitative variables
 * Performs multivariate analysis by generating scatter plots of each continuous variable against the target variable, by each categorical variable

### 5. Model


### 6. Deliver
Present findings via Jupyte Nrotebook

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

Next, open the Jupyter notebook titled “<<FINAL REPORT NAME>>” and execute the code within. 

## Takeaways
During the analysis process, I made use of the following regression models:

Additionally, I made use of clustering to generate a number of new features.

 
## Next Steps
