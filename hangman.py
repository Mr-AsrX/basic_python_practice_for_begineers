import random
import time
point = 0
roll_time = 6
wordlist = ["akshay","singh","pooja","rahul","rajesh","rahul"]

def user_char(char = ""):
    char = input("enter the  charcter: ")
    secret_word = random.choice(wordlist)
    if secret_word.find(char) >=0:
        char_index = secret_word.find(char)
        time.sleep(5)
        global point
        point+= 1
        print(f"secret char{char} present in {secret_word} at {char_index}position ")
        if secret_word.count(char)>1:
            char_index1 = secret_word.find(char, char_index)
            print(f" second time secret char{char} present in {secret_word} at {char_index1}position ")

    else:
        time.sleep(5)
        print(f"try again: {char} not in {secret_word}")


while roll_time > 0:
    user_char()
    roll_time -= 1

if point >= 3:
    print(f"Congrates! You Got {point} points  , You are Winner! ")
else:
    print(f"Oops! You Got {point} points  , You are lose! ")