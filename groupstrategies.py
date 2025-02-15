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
#here is the code, I will record video in a sec: # Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# This strategy is about a game called "21 points". 
# The main strategy is to win the game by getting as close to 21 points as possible but not over 21.
# The player or dealer wins if the player or dealer's points are closer to 21 points than the other player or dealer's points.
# Card game: 21 points
import random
def Cyan34Strategy3():
    player_point = random.randint(1,10)
    dealer_point = random.randint(1,10)
    player_turn = True
    if_bust = False
    while player_point < 21 and dealer_point < 21:
        if player_turn:
            print("Current Player's point: ", player_point)
            print("Current Dealer's point: ", dealer_point)
            print("Player's turn")
            if_want = input("Do you want another card? (y/n)")
            if if_want == "y":
                player_point += random.randint(1,10)
                if player_point > 21:
                    print("Player busts")
                    if_bust = True
                    break
            else:
                player_turn = False
        else:
            print("Dealer's turn")
            if dealer_point < 17:
                point = random.randint(1,10)
                print("Dealer's new card point: ", point)
                dealer_point += point
                if dealer_point > 21:
                    print("Dealer busts")
                    if_bust = True
                    break
            else:
                break
    if if_bust:
        if player_point > 21:
            print("Dealer wins")
        else:
            print("Player wins")
        return
    else:
        print("Final Player's point: ", player_point)
        print("Final Dealer's point: ", dealer_point)
        if player_point > dealer_point:
            print("Player wins")
        else:
            print("Dealer wins")
Cyan34Strategy3()
