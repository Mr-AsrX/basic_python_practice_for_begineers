import time

print("starting .........")
time.sleep(5)
points = 0
def inputs(message,choose= ""):
    choose = input(message)
#    if choose == "L" or choose =="R":
    return choose
    
result = inputs("Enter the R for go right L for left: ")
if result == "L":
    print("Welcome to BEAR ROOM")
    time.sleep(3)
    bear = inputs("select 1 for left 2 for right: ")
    if bear == "1":
        print("you loose! ")
    elif bear == "2":
        print("Welcome to diamond room ")
        
        points += 1
        diamond = inputs("select 1 for left 2 for right: ")
        if diamond == "1":
            print("you win! ")
        elif diamond == "2":
            print("you loose ! ")


elif result == "R":
    print("Welcome to DRAGON ROOM")
    time.sleep(3)
    dragon = inputs("select 1 for left 2 for right: ")
    if dragon == "2":
        print("you loose! ")
    elif dragon == "1":
        print("Welcome to diamond room ")
        
        points += 1
        diamond = inputs("select 1 for left 2 for right: ")
        if diamond == "2":
            print("you win! ")
        elif diamond == "1":
            print("you loose ! ")