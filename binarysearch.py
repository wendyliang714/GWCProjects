import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
print(countries)

# Start your search algorithm here.
user_input = input("What country are you searching for?:")

#Initialize variables
found = False #Use single "=" to set a variable
firstPoint = 0
lastPoint = length-1

#start loop

while firstPoint <= lastPoint and found == False: #Use double == to check conditions
    midPoint = int((firstPoint + lastPoint) / 2)
    if user_input == countries[midPoint]: #Use double == to check condition
        found = True #Use single "=" to change variable
    else:
        if user_input > countries[midPoint]:
            firstPoint = midPoint + 1
        else:
            lastPoint = midPoint - 1

# If the city is found, then print the city name. Else, print an error message!
if found == False:
    print("Your country is not in the country list!")
else:
    print("Your country is in the country list. It is %s." % user_input)
