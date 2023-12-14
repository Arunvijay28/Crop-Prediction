# Crop-Prediction
It a web based application for crop prediction and suggesting fertilizer for a crop  based on Aritifical Intelligence algorithm called Constraint Satisfaction Problem (CSP) 

## CSP(Constraint Satisfaction Problem)
It consist of 3 elements:
  1) Domains
  2) Variables
  3) Constraints

In which :
Variables: A list containt crops,
Domains: A set of 10 crops,
Constraints: Temperature,Precipitation,Humidity etc..,
Dataset: It has  data taken from government and synthetic data so it has an accuracy of 89% by providing proper dataset it can able to provide crops with an accuracy of 99.5%

## Ways of Implementing
It can be implemented in 3 ways:
  1)Forward Chaining
  2)Backtracking
  3)Intelligent Backtracking
  
In which we have used intelligent Backtracking which is discussed later

## Intelligent Backtracking
Intelligent Backtracking:
It get the constraints from the user and based on it finds the specific crops that satisfy that particular constraint and it will be added in the variables once if a contraint is not satisified it add the previous crop in the variables and does the intelligent backtracking and begins with new crop.

## Walkthrough

### Home Screen
<img src="/static/output/Screenshot 2023-11-19 213414.png" width=50%>

<img src="/ststic/output/Screenshot 2023-11-19 213451.png" width =50%>

## Crop Prediction Page

<img src="/static/output/Screenshot 2023-11-19 213625.png" width=50%>

## Sample Ranking of Crops
<img src="/static/output/Screenshot 2023-11-19 213805.png" width=50%>

