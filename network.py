import turtle
import math
class User:
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.connections = []

    def getName(self):
        return self.user_name

    def getUserId(self):
        return self.user_id

    def addConnection(self, connection_id):
        self.connections.append(connection_id)

    def getConnections(self):
        return self.connections

    def displayUser(self):
        print ("Name:", self.name, "ID:", self.user_id, "Connections:", self.connections)

user1 = User("Sydney", "sydney2017")
user1.getName()
user1.getUserId()
user1.displayUser()

user2 = User("Wendy", "wendy2000")
user2.getName()
user2.getUserId()
user2.displayUser()


class Network:
    def __init__ (self):
        self.users = []

    def numUsers(self):
         #returns the number of users in the network
        return len(self.users)

    def addUser (self, username):
        # creates a new user, assigns them an ID
        # and adds them to the network
        newUser = User(user_name + user_id)
        user_id = len(self.users) + 1
        self.users.append(newUser)

    def getUserID(self, name):
        #returns the user id when given the users username
        return self.user_id

    def addConnection(self, user1, user2):
        #This function
        # 1) gets the user ids of user1 and user2
        # 2) checks to see if these users are already connected
        # 3) If theyre not, adds user1 to user2's connections and viceversa
        return self.user_id


     def printUsers(self):
        #BONUS
        #this function goes through the users in the network and prints them
        print (self.users)

    def printConnections(self, username):
        #BONUS
        #This function takes in a username, finds the corresponding user, and
        #then prints that users connections
        print (self.connections)

#user1.addConnection("Sydney")
#user2.addConnection("Wendy")

def main():
    print ("Want to join the social network? Type 'a' to start")
    user_input = input()
    #if user_input == "a":
    #print ("")
