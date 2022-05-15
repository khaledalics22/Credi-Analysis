# Credit Analysis
This is a problem from kaggle - [problem-kaggle](https://www.kaggle.com/datasets/kapoorshivam/credit-analysis)

# Problem Description
Consider you are a Data Analyst with a private bank or a loan distribution firm. Your organization receives many applications in a given day. In order to process the applications, you sometimes miss out on accepting applications from people who are able to pay loans in time and end up sanctioning loans to those who later turn out to be defaulters.

You are now provided with two datasets:

Current_app: This file gives you information on the existing loan applications. Whether or not clients have payment difficulties
Previous_app: This file contains information on the previous loan applications with status details of the previous applications being Approved, Cancelled, Refused or Unused offer.

# Project Description
This project is implemented in Python to analyze and build model for loan default prediction. 
In this project we worked on Current_app data set to analyze loan applications wheather or not clients are defaulters. 
The data set has 307511 rows and 122 columns. 

# Libraries Used
  Numpy | Pandas | Seaborn | Missingno | Sciypy | SciKit-learn | Matplotlib

# Working Flow
Due to the large number of columns and considering the purpose of the project which is classification 
with **Big Data** techniques. followed the following flow: 

* ## Data Cleansing
  * **Check & visualize Nan values** <br> 
    To check and visualize Nan values, we used pandas and missingno libraires
    <p align="center">
        <img width="460" height="300" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-17-23.png">
    </p>
<!--     <img align="center" width="100" height="100" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-17-23.png"> -->
<!--     ![alt text](https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-17-23.png?raw=true) -->
   
  * **Fill Nan Values** <br> 
    Due to the large number of nan values, we dropped columns with more than 50% Nan values, fill columns with less than 13% nan values with mean and mode, and we dropped remaining rows with nan values. 
  * **Check invalid values**<br> 
    Here we checked for outliers and invalid values using histogram to calculate correct mean
      <p align="center">
        <img width="460" height="300" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-18-56.png">
    </p>
<!--     ![alt text](https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-18-56.png?raw=true) -->
    
* ## Bivariate Analysis

  * **Continuous Vs Continuous Analysis**<br> 
    For this analysis, we used correlation to check dependencies between features, and we removed redundant features. 
    
    <p align="center">
        <img width="460" height="300" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-19-33.png">
    </p>    
<!--      ![alt text](https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-19-33.png?raw=true) -->
     
  * **Continuous Vs Target (categorical output)**<br> 
    Here, we used poxplot from matplotlib to check dependency between continour features and target feature
    , and we removed features that the target does not correlate to. 
    <p align="center">
        <img width="460" height="300" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-20-06.png">
    </p> 
<!--      ![alt text](https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-20-06.png?raw=true) -->
    
  * **Binary-Categorical Vs Binary-Categorical**<br> 
    We used **Pearson'R** to check correlation between the binary features, we removed features correlated to other features with p-value < 0.05 and correlaiton coeff > 0.85.
  * **Binary-Categorical Vs Target (categorical output)** <br> 
    We used same technique as for binary Vs binary above,  And we removed features that are not highly correlated with target feature.
  * **Multi-Categorical Vs Continuous**<br>  
    For this analysis, we used poxplot from matplotlib to find out the correlation between multi-categorical features and continuous features 
      <p align="center">
        <img width="460" height="300" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-21-39.png">
    </p>  
<!--      ![alt text](https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-21-39.png?raw=true) -->
     
  * **Multi-Categorical Vs Categorical (Binary and Multi-Categorical)** <br> 
    For this analysis, we used **Chi-square test** to find out the correlation between multi-categorical features. And we removed features with value of cramers'V that are < 0.05

* ## Univariate Analysis
  * Loan application analysis
    <p align="center">
        <img width="460" height="300" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-22-01.png"> 
        <img width="460" height="300" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-22-12.png"> 
    </p>
  * Female vs male analysis
    <p align="center">
        <img width="460" height="300" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-22-39.png">  </p>
  * Occupation type analysis
    <p align="center">
        <img width="460" height="300" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-23-00.png">
    </p>

* ## Building Learning Models
  We Notice that the dataset is highly impalanced so we applied oversampling/undersampling techniques
  to palance the dataset and trained the following models on both techniques. 
  * Logistic Regression
  * Naive Bayes
  * Decision Tree
  * K-Nearest Neighbors (KNN)
  * Support Vector Machine (SVM)
  * Random Forest
  
* ## MapReduce with Hadoop Streaming
  We implemented MapReduce for stocastic logistic regression model and trained our model using hadoop streaming. 
     <p align="center">
        <img width="460" height="300" src="https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-41-15.png">
    </p> 
<!-- ![alt text](https://github.com/khaledalics22/Credit-Analysis/blob/main/images/Screenshot%20from%202022-05-15%2012-41-15.png?raw=true) -->
