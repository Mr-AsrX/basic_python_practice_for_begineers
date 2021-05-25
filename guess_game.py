import random

secret_num = random.randint(1,10)
limit = 5
while limit > 0:
    user_input= int(input("enter the secret number: "))
    if user_input < secret_num:
        print("try larger num: ")
    elif user_input > secret_num:
        print("try min num: ")
    else:
        print(f"you win: in {5-limit}times")
        exit()
    limit -=1
    if limit == 0:
        print("maximum try we falled")
            