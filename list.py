grocery_list = ["cheese", "crackers", "grapes"]


#defined grocery_print function
def grocery_print(date):
    print("groceries for" + date) #concatenate string and variable
    for item in grocery_list:
        print(item)



#call grocery_print function
grocery_print("Friday")
grocery_print("Monday")
grocery_print("Sunday")



for item in grocery_list:
    if item == "cheese":
        print("it's cheese!")
    else:
        print("it's nacho cheese!")
