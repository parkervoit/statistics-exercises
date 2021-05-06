import numpy as np
import pandas as pd


# 1. How likely is it that you roll doubles with two dice?
n_trials = nrows = 10000
n_dice = ncols = 2
rolls = np.random.choice([1, 2, 3, 4, 5, 6], n_trials * n_dice).reshape(nrows, ncols)
rolls_df = pd.DataFrame(rolls)
dubs = rolls_df.apply(lambda x: x[0] == x[1], axis = 1)
dubs.mean()
    # .173 probability of rolling doubles with two dice

# 2. If you flip 8 coins what is the probability of getting exactly 3 heads? What is the prob
#    of getting more than three heads?
n_trials = nrows = 10000 
n_coins = ncols = 8
toss = np.random.choice([1,0], n_trials * n_coins).reshape(nrows, ncols)
trials = toss.sum(axis = 1)
(trials == 3).mean()
    # .227 simulated probability of getting exactly  three heads 
(trials > 3).mean()
    # .6328

# 3. There are about 3 web devs for 1 data science student at Codeup. Assuming a random selection to put on a billboard
#    What are the odds that the two billboards I drive past both have DS students on them?

probabilities = [.75, .25]
billboard = np.random.choice(["web","data"], size = 10000, p = probabilities)
data = (billboard == "data").mean()
data * data 

      # 0.0616 probability of seeing two ds students

# 4. Codeup students buy on average 3 poptarts a day (+-1.5). If the vending machine has 17 on monday,
#    how likely is it that someone could buy poptarts friday afternoon

pop = np.random.normal(3, 1.5, size = [10000, 5])
pop[pop<0] = 0
pop_df = pd.DataFrame(pop)
popeat = pop_df.apply(lambda x: x.sum(), axis = 1)
(popeat <= 16).mean()
    #.6144 probability of being able to eat a poptart on friday afternoon

# 5. men have a hight of 178cm +- 8 and women are 170cm +-6.
#    Whats the probability of a woman being taller than a man?
h_men = np.random.normal(178, 8, size = 10000)
h_wom = np.random.normal(170, 6, size = 10000)
tall = h_men - h_wom 
(tall < 0).mean()
   #.2064 probability that a woman is taller

# 6. theres a 1 in 250 chance that there is a corrupted download. What are the odds that after
# 50 downloads, no one has an issue. what about 100 students, what about 150, and all of them?
nrows = 10000
ncols = 50
cond_f = 1
cond_s = 0 
prob_failure = (1/250)

install = np.random.random((nrows, ncols))
((install < prob_failure).sum(axis = 1) == 0).mean*()
    # 50 downloads, theres a .8175 chance of not having an error
    # 100 .675 chance of not having an error
    # 150 .5485 chance of not having an error
    # 450 .1644 chance of not having an error

# 7. theres a 70 chance on any given day that there will be a food truck. 
#    you havent seen on in 3 days, how likely is this? How likely is that a 
#    food truck will show up?

nrows = 10000
ncols = 3
food_truck = 1
no_food = 0
truck_prob = .7

data = np.random.random((n_rows, n_cols))
((data < truck_prob).sum(axis = 1) == 0).mean()
# 3 day prob is .0258

ncols = 2
data = np.random.random((n_rows, n_cols))
1 - (((data < truck_prob).sum(axis = 1) == 0).mean())
# there is a .9139 chance a food truck will appear in the next 2 days

# 8. 23 people are in the room. What are the odds that 2 share a birthday?
#    what about 20 people? 40?
days = range(0,365)
nrows = 100000
ncols = 22
classroom = np.random.choice(days, size = (nrows, ncols))

listofdays = [len(np.unique(classrooms[n])) for n in range(0, nrows - 1) if (len(np.unique(classrooms[n])) > 1)]