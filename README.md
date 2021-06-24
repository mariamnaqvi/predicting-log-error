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
* Confidence level = 
* Alpha = 1 - Confidence level = 
* H<sub>0</sub>: 
* H<sub>1</sub>: 

Data Dictionary

The data was initially comprised of the following columns:
Name | Datatype | Definition | Possible Values 
--- | --- | --- | --- 
parcelid|non-null  int64|Unique identifier for each property|Numeric value

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
* Use the Trello board to compile and track the tasks involved in this project
* Collect required data-source information (namely the database connection details/credentials)
* Perform surface-level examination of the 2017 data

### 2. Acquire
* Acquires the dataset under analysis, using python code within the "acquire.py" script. Uses stored credentials (via env.py) to collect data from the codeup database
* Data is collected from the following tables using a SQL query:
  1. properties_2017
  2. predictions_2017
  3. propertylandusetype
  * as was the case in the previous Zillow project, we are focusing on single-unit properties. By definition, this includes any property that matches the following description: "a housing unit within a larger structure that can be used by an individual or household to eat, sleep, and live. The unit can be in any type of residence, such as a house, apartment, or mobile home, and may also be a single unit in a group of rooms"
  * to improve performance, caching was used - the data collected by the aforementioned query was stored in a CSV file on my machine. This allows us to avoid repeated calls to the database by instead using the local copy on subsequent data acquisition calls

### 3. Prepare
* This step involves the cleaning and preparation of the data. To increase modularity, this functionality is a part of the "prepare.py" python script.

### 4. Explore


### 5. Model


### 6. Deliver


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


## Next Steps
