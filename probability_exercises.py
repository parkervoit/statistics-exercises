#import libraries for analysis. create random seed
from env import host, username, password
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd
np.random.seed(123)
# 1. A bank found that the average number of cars waiting during the noon 
# hour at a drive-up window follows a Poisson distribution with a mean of 
# 2 cars. Make a chart of this distribution and answer these questions 
# concerning the probability of cars waiting at the drive-up window.
l = 2
cust = stats.poisson(l)
# What is the probability that no cars drive up in the noon hour?
cust.pmf(0)
    #0.1353352832366127
# What is the probability that 3 or more cars come through the drive through?
cust.sf(2)
   # 0.32332358381693654
# How likely is it that the drive through gets at least 1 car?
cust.sf(0)
    # 0.8646647167633873
#  Grades of State University graduates are normally distributed with a mean of 3.0
#  and a standard deviation of .3. Calculate the following:
grades = stats.norm(3, .3)
#What grade point average is required to be in the top 5% of the graduating class?
grades.isf(.05)
    # 3.4934560880854417
# What GPA constitutes the bottom 15% of the class?
grades.ppf(.15)
    # 2.689069983151863
# If I have a GPA of 3.5, what percentile am I in?
grades_array = np.array(grades)
np.percentile(grades,3.5)
grades.cdf(3.5)
    # 0.9522096477271853
# A marketing website has an average click-through rate of 2%. One day they 
# observe 4326 visitors and 97 click-throughs. How likely is it that this many 
# people or more click through?
rate = .02
trials = 4326
clicks = 97
stats.binom(trials, rate).sf(96)
    # 0.1397582363130086
# You are working on some statistics homework consisting of 100 questions where 
# all of the answers are a probability rounded to the hundreths place. Looking 
# to save time, you put down random probabilities as the answer to each question.
stats.binom(60, .01).sf(0)
    #0.4528433576092388 
# The codeup staff tends to get upset when the student break area is not cleaned up. 
# Suppose that there's a 3% chance that any one student cleans the break area when 
# they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 
# students visit the break area. How likely is it that the break area gets cleaned 
# up each day? How likely is it that it goes two days without getting cleaned up? All week?
1-stats.binom(118, .03).sf(0)
stats.binom(59, .03).sf(0)
1 - stats.binom(295, .03).sf(0)

n = round(.9 * 3 * 22)
p = .03
stats.binom(n, p).sf(0)
stats.binom(n * 2, p).pmf(0)
stats.binom(n * 5, p).pmf(0)
    #0.00012521651388086585
# You want to get lunch at La Panaderia, but notice that the line is usually very long 
# at lunchtime. After several weeks of careful observation, you notice that the average 
# number of people in line when your lunch break starts is normally distributed with 
# a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to
# order, and 10 minutes from ordering to getting your food, what is the likelihood that 
# you have at least 15 minutes left to eat your food before you have to go back to class? 
# Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.
lunch = 60
eat = 15
food = 10 

wait= 15 * 2
stddev = 3 *2

totwait = lunch - food - eat
stats.norm(wait, stddev).cdf(totwait)
    #0.7976716190363569

# Connect to the employees database and find the average salary of current employees, 
# along with the standard deviation. For the following questions, calculate the answer 
# based on modeling the employees salaries with a normal distribution defined by the 
# calculated mean and standard deviation then compare this answer to the actual values present in the salaries dataset.
from env import host, username, password
def get_db_url(username,password,host,db_name):
    return f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
emp_db = get_db_url(username,password,host,"employees")
query = 'SELECT * FROM salaries WHERE salaries.to_date > now()'
salaries = pd.read_sql(query, emp_db)
mean = salaries.salary.mean()
std_dev = salaries.salary.std()
emp_dist = stats.norm(mean, std_dev)
# What % of emps earn less than 60000
emp_dist.cdf(60000)
    #0.24385742480214423
# What % of emplyees earn more than 95k?
emp_dist.sf(95000)
    #0.09208819199804053
# what % of employees earn between 65 and 80k 
emp_dist.cdf([65000, 80000])
# what do the top 5% of employees make?
emp_dist.isf(.05)