import pandas as pd
import numpy as np
import statsmodels.api as sm

# Read data from CSV files
large_company_data = pd.read_csv('Large_company_Turnover_2012-2021.csv')
smes_data = pd.read_csv('SMEs_Turnover_2012-2021.csv')

# Select relevant columns for analysis
columns = ['Turnover\nth GBP 2012', 'Turnover\nth GBP 2013', 'Turnover\nth GBP 2014',
           'Turnover\nth GBP 2015', 'Turnover\nth GBP 2016', 'Turnover\nth GBP 2017',
           'Turnover\nth GBP 2018', 'Turnover\nth GBP 2019', 'Turnover\nth GBP 2020',
           'Turnover\nth GBP 2021']

# Concatenate the data from both files
data = pd.concat([large_company_data[columns], smes_data[columns]])

# Convert the data to numeric format
data = data.apply(pd.to_numeric, errors='coerce')

# Drop any rows with missing values
data = data.dropna()

# Add a constant column for the intercept
data = sm.add_constant(data)

# Create a target variable for the regression (e.g., 2021 turnover)
target_variable = 'Turnover\nth GBP 2021'

# Split the data into predictor variables (X) and the target variable (y)
X = data.drop(columns=target_variable)
y = data[target_variable]

# Fit the linear regression model
model = sm.OLS(y, X)
results = model.fit()

# Print the regression table
print(results.summary())
