from random import *

#Create the list of words you want to choose from.
sides = ["seafood soup", "caesar salad", "roast potatoes"]
main_courses = ["chicken pasta", "rib eye steak", "Singapore chow fun"]
desserts = ["vanilla icecream","fruit yogurt", "chocolate cake"]

#Generates a random integer.
x = randint(0, len(sides)-1)
x = randint(0, len(main_courses)-1)
x = randint(0, len(desserts)-1)


print(sides[x])
print(main_courses[x])
print(desserts[x])
