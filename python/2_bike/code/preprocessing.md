---
# title : "python-module1-week2-assignments"
# date : "2021-02-05"
# tags : [python, exemple, stats]
---

# emails
- source1: https://github.com/CodeAcademyBerlin/Data-Science/blob/master/Module%202/Week%201/Task1-email.md
  - customer: Capital Bikeshare
  - feature: a mid-size bike rental company wants to design a data-driven platform.

  - task: determine what kinds of analytics and visualizations would empower their business.
  - task-sub: to forecast bike rental demand for their bike sharing program.

  - datasets: houghly/daily counts of rental bikes, the weather information for 24months

- source2: https://github.com/CodeAcademyBerlin/Data-Science/blob/master/Module%202/Week%201/Task2-email.md
  - situation: last week, lots of complaints from registered bike riders: non-availability of bikes 
  - Also, I do not want to get such complaints from Casual Users. Hence, how could analytics team help me in preventing this happening to Casual Users.
  - Since past, I have seen in Rainy days, we do not make much profits for obvious reasons. Can you provide us a statistics about contribution of weather in bike demands.
  - I believe, pollution and traffic would have some effect on sales. Can we have any investigation into that.


- task1: https://github.com/CodeAcademyBerlin/Data-Science/blob/master/Module%202/Week%201/Task1.md
- task2: https://github.com/CodeAcademyBerlin/Data-Science/blob/master/Module%202/Week%201/Task2.md

```python
#preprocessing.py

```
# The factors affecting the current market 
- hourly trend: peak during rush hours and week hours
- daily trend: registered vs. casual users
- rain: demand of bikes will decrease on rainy/humid days vs. sunny days.
- temperature: considering washington DC's temperature during winter period, people like to go outside when it' over XX degrees.
  - The month of January is the coldest month of the year in the nation’s capital with morning low temperatures mostly in the mid to upper 20s F (-2 to -3C) with afternoon highs in the low to mid-40s F (6 to 7C).
  - https://www.timeanddate.com/weather/usa/washington-dc/historic?month=1&year=2021
- business model: business rely on registered customers than casual users
- > it would be good to care the issue/complaints from registered users during winter period.