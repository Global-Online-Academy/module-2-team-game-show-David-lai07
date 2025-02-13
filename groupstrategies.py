# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING

import random

# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split,steal"),("split,split"),("steal,split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy: always split unless opponent has two steals in their history
def strategy1(history):
    split = 0
    steal = 1
    for i in history:
        (me, them) = i
        if them == "steal":
            steal += 1
        else:
            split +=1
    if steal == 2:
        return random.choice(["split", "steal"])
    else:
        return "split"
print(strategy1(hist2))

# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy: If there have less than 4 rounds, pick at random
# at least 4 rounds if there are 4 rounds always steal
# if there are more than 4 rounds pick at random with 80% chance of split 20% chance of steal
def strategy2(history):
    if len(history) < 4:
        return (random.choices["split", "steal"])
    elif len(history) == 4:
        return "steal"
    if len(history) > 4:
        return random.choices(["split", "steal"], weights=[0.8,0.2])[0]
print (strategy2(hist4))



# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 
