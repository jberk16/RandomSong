import random

songlist = [] #empty list
songtext = open("print.txt")
for line in songtext:
    songlist.append(line) #loops through file and puts each line as element in list

def singlesong(): #prints the randomly chosen song
    seed = random.randint(0,len(songlist)-1)
    print songlist[seed]

def carddraw(): #creates a list of n songs, each player eliminates 1
    n = raw_input("How many songs in the card draw? ")
    try: #sanity check, makes sure n is a number
        n = int(n)
    except ValueError:
        print("Invalid input")
    cards = random.sample(songlist, n)
    for index in range(0, n):
        print cards[index]
    remove1 = raw_input("Which # song would you like to remove? (0-" + str(n-1) + ") ")
    remove1 = int(remove1)
    del cards[remove1]
    for index in range(0, n-1):
        print cards[index]
    remove2 = raw_input("Which # song would you like to remove? (0-" + str(n-2) + ") ")
    remove2 = int(remove2)
    del cards[remove2]
    for index in range(0, n-2):
        print cards[index]
    #TODO: Sanity checks for remove1 and remove2

while True: #loop that keeps the program running until user says Break
    text = raw_input("Press Enter to continue, or press Break to finish ")
    if text == "Break":
        break
    elif text == "":
        carddraw()
    else:
        print "Invalid input"
#TODO: Allow to choose between singlesong and carddraw
