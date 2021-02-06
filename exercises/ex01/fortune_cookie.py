"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730395373"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
a: int = (randint(0,100))
if a < 25:
    print("You will find what you desire if you keep searching.")
else:
    if a < 50:
        print("You will use your distinct talents to benefit the world.")
    else:
         if a < 75:
             print("You never know where you may find love :).")
         else:
             print("Do not fear, for things will get better.") 

print("Now, go spread some positive vibes!")
