# Crop-Prediction
It a web based application for crop prediction and suggesting fertilizer for a crop  based on Aritifical Intelligence algorithm called Constraint Satisfaction Problem (CSP) 

## Table of Contents
[Description](#description)  
[Website Walkthrough](#walkthrough)  
[Technologies Used](#tu)  
[CSP](#csp)  
[Intelligent Backtracking](#ib)  
[Naive Bayes](#nb)  
[Future works](#fw)  

<a id="description"></a>
## Description
Given many parameters and different constraints, the system must recommend the suitable crop to be grown such that it should give maximum profit to the farmers as well as meet the market demand.
The system also has a feature to suggest a fertilizer based on the  nutrient contents present in a particular soil and type of crop to be grown in that particular soil.

<a id="walkthrough"></a>
## Walkthrough

### Home Screen
<img src="/static/output/Screenshot 2023-11-19 213414.png" width=50%>

<img src="/static/output/Screenshot 2023-11-19 213451.png" width =50%>

### Crop Prediction Page
<img src="/static/output/Screenshot 2023-11-19 213625.png" width=50%>

### Sample Input
<img src="/static/output/Screenshot 2023-11-19 214806.png" width=50%>

### Sample Ranking of Crops
<img src="/static/output/Screenshot 2023-11-19 213805.png" width=50%>

### Fertilizer Suggestion Page
<img src="/static/output/Screenshot 2023-11-19 214307.png" width=50%>

### Sample Output for Fertilizer Suggestion
<img src="/static/output/Screenshot 2023-12-14 192409.png" width=50%>

<a id="tu"></a>
## Tools Used
* HTML   -  Interactive UI
* CSS    -  Styling
* Python - To implement CSP alogorithm
* Flask  - Web Framework
* Matplotlib - Data Visualization
* Sklearn  - Data Modelling
<a id="csp"></a>
## CSP(Constraint Satisfaction Problem)
It consist of 3 elements:
  1) Domains
  2) Variables
  3) Constraints

In which :
* Variables: A list containt crops,
* Domains: A set of 10 crops,
* Constraints: Temperature,Precipitation,Humidity etc..,
* Dataset: It has  data taken from government and synthetic data so it has an accuracy of 89% by providing proper dataset it can able to provide crops with an accuracy of 99.5%

## Ways of Implementing
It can be implemented in 3 ways:
  1) Forward Chaining
  2) Backtracking
  3) Intelligent Backtracking
  
In which we have used intelligent Backtracking which is discussed later
<a id="ib"></a>
## Intelligent Backtracking
It get the constraints from the user and based on it finds the specific crops that satisfy that particular constraint and it will be added in the variables once if a contraint is not satisified it add the previous crop in the variables and does the intelligent backtracking and begins with new crop.

<a id="nb"></a>
## Naive Bayes
We have used Naive bayes model to detect the accuracy of the data collected from various websites to make sure that, the prediction made with that particular dataset  is mostly accurate.

<a id="fw"></a>
## Future Works
To include a feature to detect disease by uploading an image of the infected plant .
