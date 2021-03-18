---
# title : "python-module2-week7-email2"
# date : "2021-03-11"
# tags : [python, exemple, stats]
---



- to check the demand of users during specific hour range. e.g., 5-9am, and 16-19pm
- to check if the registered users also tend to use it during weekend or more random users: ride_id / correlation

> - comparison between user type and duration > correlation between user type and duration
> -fig1) left side (row: days, hourly change (x - histogram per user type)) // right side: "The mean duration of bike rentals.png"    
> -fig2) comparison within specific time range : commute (5-9, 15-19) vs. normal (0-4/../10-14/../20-23)

- Goal :
    - Analyze current market status
        - User behavior and preference 
            - analyze pattern 
                - visualization using timeseries decomposition
                - e.g., the demand of bike rentals per user type and station (hour - daily - weekly - monthly / year)
            - provide solutions 
                - timeseries forecast using regression modelling with the accuracy of model (reliability)
                - Additional analysis on KPI (Key Performance Indicators. e.g, traffic at the top stations, duration of membership, popularity/review in the community, UX/UI part: only provide useful information on the app - e.g., location of available stations/number of bikes)

1) how to satisfy the current customers: regular and casual users
    - You want to find the bike as soon as you need it
    - keep the availability of bikes during peak time 
        - What are the stations with high demand in both start & end stations?

        - What are the start stations where the demand of regular users is high (What is the proportion of regular users in the station)? & what are the end stations where regular users leave bikes
        - What are the start stations where the demand of casual users is high & how many bikes are left at the station (The rank as an end station)
        - What are the number of available free bikes at top10 start stations (if possible, visualize the available number of bikes at those stations at each hour)
    -> by providing more bikes during XX hours , at XX stations


    -? future points: how is the return rate of bikes for both users:
        if casual users tend to use bike one-way trip, how can we relocate those bikes to popular stations (?)  
        if regular users tend to use bike round-way trips (if returnin rate is high), how can we prepare bikes for those who didn't bring bikes to their end station (?)
        - track the rental routes and ride ID : 

    - You want to ride a bike in a good condition
    - check/replace bikes regularly 
        - What is the maximum trips for bikes to be checked/repaired? 
        - When is the expected time when the total distance of trips reaches the threshold in 2021? (forecast model)
            - model: how the total distance of trips is influenced from the distance and the duration of trips for both regular and casual users.
            - distance of trips: https://stackoverflow.com/questions/57294120/calculating-distance-between-latitude-and-longitude-in-python
            
    -> by replacing the biks every XX months.
 
        - What is the average duration / distance of trips (regular vs. casual)

2) how to increase the market: 
    - how to attract new comers 
    - how to increase the availability to new comers: the period of rental membership (free-trial period for 1/2weeks or 1month)

- modeling : predict the demand of registered users (members) and the casual users (casual) during saturday
- data: 2021-Jan-lastweek, 

- result: 
    - Based on the yearly pattern of regular/casual users, January has the lowest demand(in 2020, 2019, 2018)
    - The pattern of users demand in target period (Jan2021) is similar to the ones collected from previous 3 years, but the total demand has decreased(?) compared to the demand from previous 3 years. 
        - Proof: daily pattern of users in 2021 (and 3 years), the total number of rides(trips)  in 2021 (and 3 years).
    - The proportion of new users are increasing (?)
    - 

?? traffic in top 5 stations > only for email(KPI)


- source: https://towardsdatascience.com/a-step-by-step-guide-for-creating-advanced-python-data-visualizations-with-seaborn-matplotlib-1579d6a1a7d0

