---
# title : "python-module1-week2-assignments"
# date : "2021-02-03"
# tags : [python, exemple, stats]
---
# statistics - questions 
- Source: https://dsft.code-data-ai.com/stats-1/


- Q1: Given, there are 5 numbers in the data set: (8, 12, 16, 24, 4). What will be the sum of deviations of individual data points from their mean ?
> A1: Zero.

- Q2: If some outliers are introduced to the dataset, what will happen to the Standard Deviation ?  
  - A) Standard Deviation is robust to outliers 
  - B) Standard Deviation will increase with the introduction of outliers. 
  - C) Standard Deviation will decrease with the introduction of outliers. 
  - D) Can not be determined.  
> A2: B
> 
> - Standard deviation is a square root of variance.
> - Variance is a sum of squares of differences between all numbers in the data and their mean.
> - Standard deviation measures the extent to which data varies from the mean.


- Q3: Suppose the below positively skewed distribution has a median of 30, which of the following statement is true?
  - A) Mean is greater than 30
  - B) Mean is less than 30
  - C) Mode is greater than 30
  - D) Mode is less than 30
  - E) Both A and D
  - F) Both B and C

> A3: A
> - A positively skewed distribution is a result of unequal distribution of values in given data. In this distribution, the mean is usually greater than the median because a few values(datapoints) tend to shift the mean to the right and these datapoints would be considered as outliers.
> - concept 'skewness': https://askinglot.com/what-does-positively-skewed-mean-in-statistics
> https://web.ma.utexas.edu/users/mks/statmistakes/skeweddistributions.html
> 


1. Which value can be the possible value for the median of the below distribution?
    - A) 40
    - B) 26
    - C) 16
    - D) 50
> A4: B

5. What is the shape of the distribution ?
> A5: positively skewed distribution

6. What would you consider to be the most appropriate measure of the center for this data?
> A6: median

7. If Y axis represents the number of individuals and X axis – salary of the individual in thousands. How many individuals have salary less than 10 thousands ?
> A7: (maybe) 35 (the height of bars is not clear)

8. We have a set of positive numbers. If a single value of the set is altered what must change ? 
    - A) Mean 
    - B) Median 
    - C) Mode 
    - D) All of these
> A8: D

9. The chart shows hourly consultancy rate of 10 people. Calculate the standard deviation of the salaries of the 10 employees.
> A9

10.  Which of the following random variables is discrete?

A) the length of time a battery lasts
B) the number of pens purchased by a student in a year
C) the percentage of cows in a cattle firm that have been vaccinated
D) the distance between a pair of towns
> A10: B
> - "discrete variable": https://en.wikipedia.org/wiki/Continuous_or_discrete_variable

11.  Which of the below normal distributions will have the greatest spread? ( mu = mean, sigma = stdev)
     - A) mu=5,  sigma =1.5
     - B) mu=10, sigma =1.0
     - C) mu=5,  sigma =1.65
     - D) mu=8,  sigma =1.2
     - E) mu=10, sigma =1.6
> A11: E (or it changes depending on the population of given dataset)

```python
import numpy as np
from matplotlib import pyplot as plt 

# apply same codes for A-E
mu = 10 #mean
sigma = 1.6 #stddev
sample = 100
np.random.seed(0)
sample_E = np.random.normal(mu, sigma, sample).astype(int)

# draw histogram
data_all = pd.DataFrame({'sample_A': sample_A,'sample_B': sample_B,'sample_C': sample_C, 'sample_D': sample_D, 'sample_E': height_E})
data_all.hist()
```

12. For a normal distribution with mu=10 & sigma =1.4, about 2.5% of the values lie above what value? (Assume that the number is above the mean value) ( mu = mean, sigma = stdev)
> A12 : 2 (2 sigma)


### additional info
- how to calculate standard deviation: 
  - calculate the mean > calculate the variance > calculate the square root of the variance
    ```python
    import numpy as np
    val = np.array([8, 12, 16, 24, 4])
    np.mean(val)

    def std(a): 
        n=len(a)
        m=sum(a)/len(a)
        d=[e-m for e in a] # deviations from mean
        v=0
        for e in d:
            v+=e**2
        return (v/n)**.5

    std(val)

    ```

