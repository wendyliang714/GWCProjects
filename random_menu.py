#import random function
import random
secure_random = random.SystemRandom()

#Create the list of words you want to choose from.
sides = ["seafood soup", "caesar salad", "roast potatoes"]
main_courses = ["chicken pasta", "rib eye steak", "Singapore chow fun"]
desserts = ["vanilla icecream","fruit yogurt", "chocolate cake"]


#Generates a random string.
print(random.choice(sides))
print(random.choice(main_courses))
print(random.choice(desserts))
