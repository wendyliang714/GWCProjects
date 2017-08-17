start = '''
You and your girlfriend walk into a bank to deposit money.
Suddenly, a robber enters and yells, "Everyone down! This is a stickup!"
Everyone in the bank gets down on the floor, yet you're conflicted.
What will you do?
'''

print(start)

print("Type 'hide' to get down or type 'stand' to stand up to the robber.")

def return_previous():
    user_input = input()

    if user_input == "save":
        print("The robber shoots you instead, however your girlfriend and the other people in the bank survive. Your family received an honor award from the NYPD for your sacrifice. Your girlfriend never loved again.")

    elif user_input == "hide":
        print("The robber shoots at your girlfriend but misses. As all of this is occuring, one of the bankers call the police and they come and arrest the robber before he can do further damage. Your girlfriend dumps you for being so cowardly, and soon you lose your job, apartment, and rental on your car. You die single and lonely at the age of 46.")

    else:
        print("Incorrect input! Please try again.")
        return_previous()

def return_last():
    user_input = input()

    if user_input == "surrender":
        print("The bank is completely robbed and the robber escapes and is never caught. The bank closes down due to the massive amount of money lost. After the ordeal, you seemingly go 'crazy' and dump  your girlfriend and quit your job. Your doctor diagnoses you with PTSD. You're forced to live the rest of your life in a mental asylum.")

    elif user_input == "stay":
        print("The robber shoots you in the leg and attemps to escape.  However police are outside waiting for him. You're hailed as a hero and are given an honorary award from the mayor for your bravery. You and your girlfriend mary shortly after, and die together at the age of 101.")

    else:
        print("Incorrect input! Please try again.")
        return_last()


def return_beginning():
    user_input = input()
    if user_input == "hide":
        print("The robber points his gun at your girlfriend and says he is going to hold her hostage.")
        print("Type 'save' to block her from the gun or type 'hide' to hide behind her.")


        return_previous()


    elif user_input == "stand":
        print("You refuse to get down on the floor and demand to the robber that he leaves. The robber aims his gun at you and claims he will shoot in 3 seconds.")
        print("Type 'surrender' to surrender and get down on the floor, or type 'stay' to defend your ground.")


        return_last()

    else:
        print("Incorrect input! Please try again.")
        return_beginning()

return_beginning()
print("click up key to enter again")
