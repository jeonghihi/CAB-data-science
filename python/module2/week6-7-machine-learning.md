---
# title : "python-module1-week6-7-machine-learning"
# date : "2021-03-11"
# tags : [python, exemple, machinelearning]
---

# two types of algorithms used for training (how features are selected/used in the training)
- bagging
    - decision tree
    - random forest

- boosting
    - Gradient Boosting (Decision Tree)
    - Ada(ptive) Boosting
    - XGBoost (Extreme Gradient Boosting)

- difference between these methods: https://www.analyticsvidhya.com/blog/2020/02/4-boosting-algorithms-machine-learning/
- https://www.analyticsvidhya.com/blog/2015/11/quick-introduction-boosting-algorithms-machine-learning/
- https://en.wikipedia.org/wiki/Boosting_%28machine_learning%29#Boosting_for_binary_categorization


- difference between bagging and bossting: https://www.pluralsight.com/guides/ensemble-methods:-bagging-versus-boosting

- In bagging methods, (kinds of parallel ensemble technique), the weight of predictors in each model is same at each iteration (each random sampling).
- In boosting methods, (kinds of sequential ensemble technique), the weight of predictors in each model is different at each iteration (each random sampling); the newly weighted values (learned from N-1th model) are used for the predictor of Nth model.

??Q1
- In boosting methods, when the newly updated weights is built based on the error rate/accuracy of the model, how do we know if the correct instances are predicted not by chance (but with high confidence interval)? 
- K-folds is used to select the best feature setting for hyperparameters (e.g., how many and which features should be included in the model structure), then what can be used for significant testing for predictions from each model?
> A1:
> In each iteration (random sampling) during boosting, accuracy and kappa scores are measured. 
> The basic concept of boosting comes from the distinction between strong and weak learners  (source: https://en.wikipedia.org/wiki/Boosting_%28machine_learning%29#Boosting_for_binary_categorization). 



?? trade off between variance and bias. 
?? which factor is more influencing between the distribution of each predictor (data values) or the correlationi between predictors?
?? how to use categorical feature (va1: high, med, low) with continuous feature (var2) to predict more accurately


?? GAN methods


