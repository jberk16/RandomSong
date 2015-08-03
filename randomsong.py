import random

songlist = [] #empty list
songtext = open("print.txt")
for line in songtext:
    songlist.append(line) #loops through file and puts each line as element in list

def is_number(s): #stolen from some dude on StackOverflow. checks if string is a number
    try:
        int(s)
        return True
    except ValueError:
        return False

def howmanysongs(): #asks how many songs you want
    valid = False #used for loops
    songs = raw_input("How many songs in the card draw? ")
    while valid is False:
        if is_number(songs) == False:
            print "Invalid input"
            songs = raw_input("How many songs in the card draw? ")
        elif int(songs) <= 2: #card draw for 3 songs or more only
            print "Invalid input"
            songs = raw_input("How many songs in the card draw? ")
        else:
            return int(songs)

def elimsong(n):
    remove = raw_input("Which # song would you like to remove? (1-" + str(n+1) + ") ")
    valid = False #still used for loops
    while valid is False:
        if is_number(remove) == False:
            print "Invalid input"
            remove = raw_input("Which # song would you like to remove? (1-" + str(n+1) + ") ")
        elif int(remove) < 1 or int(remove) > n+1: #makes sure input is in range
            print "Invalid input"
            remove = raw_input("Which # song would you like to remove? (1-" + str(n+1) + ") ")
        else:
            return int(remove)-1
#note: to make this easier to use I ask for a number from 1 to n+1
#internally the songs are indexed from 0 to n
        
def singlesong(): #prints the randomly chosen song
    seed = random.randint(0,len(songlist)-1)
    print songlist[seed]

def carddraw(): #creates a list of n songs, each player eliminates 1
    n = howmanysongs()
    cards = random.sample(songlist, n)
    for index in range(0, n):
        print cards[index]
    remove1 = elimsong(n-1)
    del cards[remove1]
    for index in range(0, n-1):
        print cards[index]
    remove2 = elimsong(n-2)
    del cards[remove2]
    for index in range(0, n-2):
        print cards[index]

while True: #loop that keeps the program running until user says Break
    text = raw_input("Enter Random for 1 song random, Card for card draw, or Break to finish ")
    if text == "Break":
        break
    elif text == "Card":
        carddraw()
    elif text == "Random":
        singlesong()
    else:
        print "Invalid input"
