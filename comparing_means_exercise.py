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