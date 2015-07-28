import random

def main():
    seed = random.randint(1,6)
    if (seed == 1):
        print("Anubis")
    elif (seed == 2):
        print("Utopia")
    elif (seed == 3):
        print("Clockwork Genesis")
    elif (seed == 4):
        print("Delirium")
    elif (seed == 5):
        print("Pandemonium")
    else:
        print("Fly With Me")

while True:
    text = raw_input("Press Enter to continue, or press Break to finish ")
    if text == "Break":
        break
    else:
        main()
