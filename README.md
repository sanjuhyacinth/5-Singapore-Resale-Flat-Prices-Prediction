# 5-Singapore-Resale-Flat-Prices-Prediction
## Render:
View my application on Render: [app link](https://flatresale-1ii8.onrender.com)

# Problem Statement:
The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. This predictive model will be based on historical data of resale flat
transactions, and it aims to assist both potential buyers and sellers in estimating the resale value of a flat.

# Motivation behind the Project:
The resale flat market in Singapore is *highly competitive*, and it can be challenging to accurately estimate the resale value of a flat. There are many factors that can affect resale prices, such as location, flat type, floor area, and lease duration. A
**predictive model** can help to overcome these challenges by *providing users with an estimated resale price* based on these factors.

# Project Overview
## Project Title:
Singapore Resale Flat Prices Prediction

## Project Domain:
Real Estate

## Skills Takeaway:
Data Wrangling, EDA, Model Building, Model Deployment

## Python Modules:
* Numpy
* Pandas
* Scikit-learn
* Pickle
* Streamlit
* Matplotlib
* Seaborn

## Project Guide
### A. Data Preprocessing:
* Data Source : Downloaded historical resale flat data from official HDB sources, covering the period from 1990 to the current date.
* Initial Cleaning: Handled missing values, corrected inconsistencies, and ensured the data's integrity.
* Feature Engineering: Enhanced the dataset by creating new features and transforming existing ones to better capture the underlying patterns.

### B. Feature Engineering:
* Outlier Detection: Identified and handled outliers to ensure the model's robustness.
* Skewness Correction: Addressed skewed distributions using appropriate transformations.
* Category Encoding: Encoded categorical features using techniques like Label Encoding to convert them into numerical formats suitable for machine learning algorithms.

### C. Model BUilding:
* Model building: Examined different regression models (e.g., Linear Regression, Random Forest Regressor, etc.)
* Performance testing: Evaluated performance metrics to choose the best model for predicting resale price.
* Model selection: The *Random Forest Regressor* model was selected based on its superior performance in terms of R-squared, Root Mean Squared and Mean Squared Error metrics.

### Model Deployment:
* Model Serialization: Saved the trained models using pickle for later use in the application.
* Streamlit App: Built an interactive dashboard using Streamlit to allow users to input relevant features and get predictions on flat resale prices.
* Render deployment: The finalised streamlit app (usually in the local setup) was deployed to **Render**, a cloud application hosting service for developers to make their app accessible for the public, for free. The link to it is [here](https://flatresale-1ii8.onrender.com). The link is also available at the top of this ReadME page.

## Streamlit App - Design
Our streamlit application has 3 pages

* In the 'Home' section of our project, We have information relating to **Singapore Housing and Development Board** - all information on who they are, their vision & mission, and a basic statistics on how Singapore's housing prices have skyrocketed over the years. Also some more information materials on HDB has been provided as YouTube links.

* The 'Predictive Analytics' section of the app is the most important part where we display the predictions of the flat resale prices using regression algorithms such as Random Forest Regressor, by creating a user-interactive way where based on the user inputs we get the price predictions.
  
* The 'About' section of the app gives information on the project, the domain of it and an overview of the steps that were done.

## Contact me:
* Email : sanjuhwork@gmail.com
* LinkedIn : https://www.linkedin.com/in/sanju-hyacinth/
