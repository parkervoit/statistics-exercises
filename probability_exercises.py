from env import host, username, password
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd
np.random.seed(123)

l = 2
cust = stats.poisson(l)

cust.pmf(0)
cust.sf(2)
cust.sf(0)

grades = stats.norm(3, .3)
grades.isf(.05)
grades.ppf(.15)
grades_array = np.array(grades)
np.percentile(grades,3.5)

rate = .02
trials = 4326
clicks = 97
stats.binom(trials, rate).sf(96)

stats.binom(60, .01).sf(0)

1-stats.binom(118, .03).sf(0)
stats.binom(59, .03).sf(0)
1 - stats.binom(295, .03).sf(0)

n = round(.9 * 3 * 22)
p = .03
stats.binom(n, p).sf(0)
stats.binom(n * 2, p).pmf(0)
stats.binom(n * 5, p).pmf(0)


lunch = 60
eat = 15
food = 10 

wait= 15 * 2
stddev = 3 *2

totwait = lunch - food - eat
stats.norm(wait, stddev).cdf(totwait)

from env import host, username, password
def get_db_url(username,password,host,db_name):
    return f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
emp_db = get_db_url(username,password,host,"employees")
query = 'SELECT * FROM salaries WHERE salaries.to_date > now()'
salaries = pd.read_sql(query, emp_db)
mean = salaries.salary.mean()
std_dev = salaries.salary.std()
emp_dist = stats.norm(mean, std_dev)
emp_dist.cdf(60000)
emp_dist.sf(95000)
emp_dist.cdf([65000, 80000])
emp_dist.isf(.05)