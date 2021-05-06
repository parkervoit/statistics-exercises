# The average battery life for a fully charges iphone-12 is 14 hours 
# with standard deviation of 1.5 hour

# 1. what kind of probability distribution represents the random variable 
#   here for battery life in hours?

    #normal (Gaussian) distribution

# 2. What are the appropriate defining parameters for this distribution?
life = 14
stddev = 1.5

# 3. Create a Scipy object/instance for this distribution
battery_life = stats.norm(life, stddev)

# 4. Use the object create above and choose appropriate method to calculate the following:  
 # a. What is the probability the cell phone battery more than 16 hours.  
battery_life.sf(16)
    #0.09121121972586788
 # b. What is probability that cell phone battery lasts for exactly 12 hours. 
battery_life.pdf(12) 
    #0.10934004978399577
 # c. What is the probability that cell phone battery lasts for 12 hours or less.  
battery_life.cdf(12)
    #0.09121121972586788
 # d. How many hours do the battery lasts for top 25% longest lasting phones. 
battery_life.isf(.25) 
    #15.011734625294123



#  The probability that a visitor will make a purchase when browsing in your
#  web-store is 1.5%. You expect 350 web-visitors today 

#1. What kind of probability distribution you have for "# number of visitors
#   who end up making a purchase"?
# binomial distribution

#2. What are the appropriate defining parameters for this distribution?
success = .015
trials = 350

#3. Create a Scipy object/instance for this distribution
purchased = stats.binom(trials,success)

#4. Use the object create above and choose appropriate method to calculate the following:  
     #a. What is the probability that exactly 10 vistors will make the a purchase?
purchased.pmf(10)
    #0.022583869648271287

     #b. What is probability 13 or more visitors will make a purchase?
purchased.sf(13)
    #0.000992181581844392

     #c. What is probability that 10 or less visitors will make a purchase?
purchased.cdf(10)
    # 0.9819938585504345