import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
df = sns.load_dataset('mpg')
df.origin.value_counts()
#Mini Exercise:
#Are the USA origin vehicles heavier than vehicles with European origin?

usa_weight = df[df.origin == 'usa'].weight
europe_weight = df[df.origin == 'japan'].weight

#One sample t-test or 2-sample t-test? One tailed or two tailed?
    #it is a 2 sample t test, one tailed since it only is asking if they are heaviers

#Plot distributions

usa_weight.hist()
europe_weight.hist()

#Hypothesis

#$H_{0}$: US cars are not heavier than european cars

#$H_{a}$: US cars are heavier than european cars

#Significance Level

#$\alpha$  = .05, for a one tailed. If we did a two tailed it would push the alpha down to .025

#Verify Assumptions

#Normal: Normal enough, data set for both groups are very large, so CLI comes into play
#Independent: yes, both groups are independent of each other
#Variance: The variance of both groups actually significantly differ from each other, according to levenes test

stats.levene(usa_weight, europe_weight)
#LeveneResult(statistic=70.87295122660926, pvalue=1.270199808578259e-15)

# use stats.ttest to calculate t and p
stats.ttest_ind(usa_weight, europe_weight, equal_var = False)

#Ttest_indResult(statistic=18.477210677200812, pvalue=8.394202607075812e-52)

# Conclusion, USA cars are much more likely to be heavier. 


#TTest exercises
import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data

# Ace Realty wants to determine whether the average time it takes to sell 
# homes is different for its two offices. A sample of 40 sales from office #1 
# revealed a mean of 90 days and a standard deviation of 15 days. A sample of 
# 50 sales from office #2 revealed a mean of 100 days and a standard deviation 
# of 20 days. Use a .05 level of significance.

stats.ttest_ind_from_stats(90,15,40,100,20,50, equal_var = False)

#Ttest_indResult(statistic=-2.7091418459143854, pvalue=0.00811206270346016), 
# times between offices are different

# Load the mpg dataset and use it to answer the following questions:
df = data('mpg')
df = df.rename(columns = {'cty':'city', 'hwy':'highway', 'cyl':'cylinder', 'drv':'drive'})
df['average_mileage'] = df[['highway','city']].mean(axis = 1)
df['mileage_difference'] = df['highway'].sub(df['city'], axis = 0)

# Is there a difference in fuel-efficiency in cars from 2008 vs 1999?

old_cars = df[df['year'] == 1999]
new_cars = df[df['year'] == 2008]
stats.levene(old_cars["average_mileage"], new_cars["average_mileage"])
# LeveneResult(statistic=0.033228136671080453, pvalue=0.855517569468803)
stats.ttest_ind(old_cars["average_mileage"], new_cars["average_mileage"])
# Ttest_indResult(statistic=0.21960177245940962, pvalue=0.8263744040323578)
    # No there is not. Their means are pretty similar

# Are compact cars more fuel-efficient than the average car?
df["class"].unique()
compact_mask = df["class"] == "compact"
compact = df[compact_mask]
avg_car = df[compact_mask == False]
stats.levene(compact["average_mileage"], avg_car["average_mileage"])
# LeveneResult(statistic=11.107991264810888, pvalue=0.001000307619344077)
stats.ttest_ind(compact["average_mileage"], avg_car["average_mileage"])
# Ttest_indResult(statistic=6.731177612837954, pvalue=1.3059121585018135e-10)
    # compact cars get better gas mileage than the avg car

#Do manual cars get better gas mileage than automatic cars?
auto = df[df['trans'].str.contains("auto")]
manual =  df[df['trans'].str.contains("manual")]

stats.levene(auto["average_mileage"], manual["average_mileage"])
# LeveneResult(statistic=0.20075824847529639, pvalue=0.6545276355131857)
stats.ttest_ind(auto["average_mileage"], manual["average_mileage"])
# Ttest_indResult(statistic=-4.593437735750014, pvalue=7.154374401145683e-06)
    # ttest shows that manual cars have better gas mileage than automatic cars. 

