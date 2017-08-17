print ("Welcome to Sydney and Wendy's kitchen! Wanna learn to make frozen hot chocolate with us? Type 'a' to get ingredients.")

user_input = input()

ing = {'Chocolate': '3 ounces',
'Store bought hot chocolate mix': '2 teaspoons',
'Sugar': '1.5 tablespoons',
'Milk': '1.5 cups',
'Ice': '3 cups',
'Other ingredients for garnish': 'whipped cream and chocolate shavings'}

if user_input == 'a':
    print (ing)
    print ("Type '1' for instructions.")
else:
    print ('Please type again')

instructions = ["Chop the chocolate into small pieces and melt in a small heavy saucepan or in the top of a double boiler over simmering water. Stir occasionally until melted. Add the hot chocolate mix and sugar, stirring constantly until blended.",
"Remove from heat and slowly add 1/2 cup of the milk, stirring until smooth. Cool to room temperature.",
"In a blender, place the remaining 1 cup of milk, the chocolate mixture, and the ice. Blend on high speed until smooth and the consistency of a frozen daiquiri.",
"Pour into a giant goblet and top with whipped cram and chocolate shavings."]

user_input = input()
if user_input=='1':
    print (instructions[0])
    print ("Type '2' for next step.")

    user_input = input()
    if user_input == "2":
        print (instructions [1])
        print ("Nice job so far! Type '3' for next step.")

        user_input = input()
        if user_input == "3":
            print (instructions [2])
            print ("You're almost done! Type '4' for the last step.")

            user_input = input()
            if user_input == "4":
                print (instructions [3])
                print ("Your frozen chocolate is ready!")
