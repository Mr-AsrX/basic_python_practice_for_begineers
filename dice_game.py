import time
import random

print("Welcome to Dice Game! ")
time.sleep(3)

print(f"{(5*'*')} USER VS COMPUTER {(5*'*')}")

print("Game rule : press 5 for Dice Roll ")

all_dice_roll_data = {"user":[],"computer":[]}
dice_time = 0
def user_rolling(inputs = ""):

    print("User turn! \n")
    inputs = int(input("press 5 for rolling: "))
    if inputs== 5:   
        user_dice_value = random.randint(1,6)
        all_dice_roll_data["user"].append(user_dice_value)
        return user_dice_value
    else:
        exit()

def comp_rolling():
    print("Now computer turn !\n")
    time.sleep(4)
    comp_dice_value = random.randint(1,6)
    all_dice_roll_data["computer"].append(comp_dice_value)
    return comp_dice_value


while dice_time < 6:
    dice_time += 1
    user_rolled = user_rolling()
    print(f"{user_rolled} you Got ")
    comp_rolled = comp_rolling()
    print(f"{comp_rolled} Computer Got ")
    if comp_rolled > user_rolled:
        print("computer winning ")
    elif comp_rolled <= user_rolled:
        print("wow you winning ")
    
    print(f"only {6-dice_time} times remaining to roll ")
    
print ("please wait for winner: ")
user_total = 0
for rolled_No in all_dice_roll_data["user"]:
    user_total= user_total + rolled_No
comp_total = 0
for comp_rolled_No in all_dice_roll_data["computer"]:
    comp_total= comp_total + comp_rolled_No

if comp_total > user_total:
    print(f"You got {user_total} total ")
    time.sleep(3)
    print(f"Computer  got {comp_total} total ")
    time.sleep(3)
    print("OOPS! you are lose...")
elif comp_total<user_total:
    print(f"You got {user_total} total ")
    time.sleep(3)
    print(f"Computer  got {comp_total} total ")
    time.sleep(3)
    print("CONGRATULATIONS ! you are Winner...")

else: 
    print(f"You got {user_total} total ")
    time.sleep(3)
    print(f"Computer  got {comp_total} total ")
    time.sleep(3)
    print("HA HA HA ! Game draw ")
