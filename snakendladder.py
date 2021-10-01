import random
counter = 0
ans = ''
ladders = [9,18,32]
snakes = [12,24,29,38,36,42,48]
ans = input("Enter y or Y to continue playing else enter n or N to exit")
while ans == 'Y' or ans == 'y':
    n = random.randrange(1,6)
    print("Dice number iss... ",n," and you are on ",counter)
    counter+=n
    if counter in ladders:
        if counter == 9:
            counter = 14
            print("Found a ladder, Climbing up to..",counter)
        if counter == 18:
            counter = 28
            print("Found a ladder, Climbing up to..",counter)
        if counter == 32:
            counter = 41
            print("Found a ladder, Climbing up to..",counter)
    if counter in snakes:
        if counter == 12:
            counter = 6
            print("Oh no, Snake is swallowing us.., Climbing down to..",counter)
        if counter == 24:
            counter = 10
            print("Oh no, Snake is swallowing us.., Climbing down to..",counter)
        if counter == 29:
            counter = 10
            print("Oh no, Snake is swallowing us.., Climbing down to..",counter)
        if counter == 36:
            counter = 13
            print("Oh no, Snake is swallowing us.., Climbing down to..",counter)
        if counter == 38:
            counter = 20
            print("Oh no, Snake is swallowing us.., Climbing down to..",counter)
        if counter == 42:
            counter = 21
            print("Oh no, Snake is swallowing us.., Climbing down to..",counter)
        if counter == 48:
            counter = 5
            print("Oh no, Snake is swallowing us.., Climbing down to..",counter)
    if counter == 50:
        print("YOU WON!!!!!, YOU REACHED",counter)
        break
    ans = input("Enter y or Y to continue playing else enter n or N to exit")
if ans == 'n' or ans=='N':
    print("")
        
