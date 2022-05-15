# Credit Analysis
This is a problem from kaggle - [problem-kaggle](https://www.kaggle.com/datasets/kapoorshivam/credit-analysis)

# Problem Description
Consider you are a Data Analyst with a private bank or a loan distribution firm. Your organization receives many applications in a given day. In order to process the applications, you sometimes miss out on accepting applications from people who are able to pay loans in time and end up sanctioning loans to those who later turn out to be defaulters.

You are now provided with two datasets:

Current_app: This file gives you information on the existing loan applications. Whether or not clients have payment difficulties
Previous_app: This file contains information on the previous loan applications with status details of the previous applications being Approved, Cancelled, Refused or Unused offer.

# Project Description
In this project we worked on Current_app data set to analyze load applications wheather or not clients are defaulters. 
The data set has 307511 rows and 122 columns. 

# Working Flow
Due to the large number of columns and considering the purpose of the project which is classification 
with **Big Data** techniques. followed the following flow: 

* ## Data Cleansing
  * Check & visualize Nan values 
  * Fill Nan Values
  * Check invalid values

* ## Bivariate Analysis

  * Continuous Vs Continuous Analysis
  * Continuous Vs Target (categorical output)
  * Binary-Categorical Vs Binary-Categorical
  * Binary-Categorical Vs Target (categorical output)
  * Multi-Categorical Vs Continuous 
  * Multi-Categorical Vs Categorical (Binary and Multi-Categorical)

* ## Univariate Analysis
  * Loan application analysis
  * Female vs male analysis
  * Occupation type analysis

* ## Building Learning Models
  We Notice that the dataset is highly impalanced so we applied oversampling/undersampling techniques
  to palance the dataset and trained the following models on both techniques. 
  * Logistic Regression
  * Naive Bayes
  * Decision Tree
  * K-Nearest Neighbors (KNN)
  * Support Vector Machine (SVM)
  * Random Forest
