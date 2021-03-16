---
# title : "python-module2-week6-email1"
# date : "2021-03-09"
# tags : [python, exemple, stats]
---


Dear Richard,

Thank you for your email.
I have summarized three points below based on your inquiry and suggested solutions for each point. 

- Situation1: Last week, the demand of registered bike riders, who were mostly working profiessional, was higher than the usual usage. 
  >- Task: Find out how to reduce the complaints - to keep the availiability of rental bikes high enough.
  >- Action: 
  >We analyzed the demand of registered bike users and specifically the status of bike usages related to commute hours (e.g., 7-9 am and 17-19pm) given that 80% of those registered users are working professionals. 
  >- Results: 
  >We found out that the demand of registered users is most high on wednesday and saturday, specifically during commute hours (e.g., between 6-9 AM and 16-19pm). 
  >So, we suggest you to prepare more bikes during commute hours on weekdays, and during datytime (e.g., 8am to 20pm) on saturday.
<figure>
<img src="output/hdf_mean_count_day-user.png" width="400">
  <figcaption>The average demand of bike users (members vs. casual users) during last week</figcaption>
</figure>


.
<figure>
<img src="output/hdf_mean_count_hour_day-user.png" width="600">
  <figcaption>The trend of bike users demand in weekdays and weekend during last week</figcaption>
</figure>


.
<figure>
<img src="output/hdf_mean_count_hour-user.png" width="600">
  <figcaption>The average demand of bike users (members vs. casual users) for each hour of each day during last week</figcaption>
</figure>


- Situation2: You also want to avoid the complaints from Casual users. 
  >- Task: Find out when is the highest demand of casual users. 
  >- Action: We analyzed the average demand of registered bike users.
  >- Results: We found out that the pattern of casual users usage is similar to registered users, except that there is no peak of demand during commute hours. So we suggest you to prepare more bikes during weekdays and during datytime (e.g., 8am to 20pm) on saturday.



.
<figure>
<img src="output/hdf_mean_count_hour_day_timeseries-user.png" width="400">
  <figcaption>The trend of bike users' demand during last week</figcaption>
</figure>


.
- Situations3: There are a few important factors influencing the actual usage of users, such as "weathers (rainy days)" and "pollution", and "traffic" situations. 
  >- Task: Analyze how weather and pollusion, trafic affects the demand of bike rental users. 
  >- Action: Analyze how each factor is correlated with the demand of registerd and casual users, and provide a explanation for each user type.
  >- Results: We have found that the weather affects, but we need more time to provide more reliable suggestions. Currently we are training the model to predict the relationship between the (expected) weather during upcoming days and the demand based on previous usage history. For now, we prepared two figures where you can see the trend of bike users' demand during last one year (2011) and the influence of other factors on the total demand of bike rentals.

<figure>
<img src="output/hdf_uci_2011_multifactors_trend.png" width="600">
  <figcaption>The trend of bike users and the influence of factors on total demand of bike users in 2011</figcaption>
</figure>


.
<figure>
<img src="output/hdf_uci_2011_mean_count_hour_season.png" width="800">
  <figcaption>The average demand of bike users for each hour in each sason in 2011</figcaption>
</figure>


.
Thank you for taking time to check these details. 

Please feel free to contact me if any information is missing/unclear and/or you have any question. 

Hope you have a good start of this week !

Best,

Jay