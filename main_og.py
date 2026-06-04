import random
computer = random.choice([-1,0,1])
user = input("Enter your choice: ")
dict = {"s": 1, "w": -1, "g": 0}  # s=snake, g=gun, w=water
reversedict = {1: "snake", -1: "water", 0: "gun"}
if user not in dict:
    print("invaild choice")
    quit()
else:
    your = dict[user]
    print(f"You choose {reversedict[your]}\nComputer choose {reversedict[computer]}")
if computer == your:
    print("It's a Draw!")
else:
    if computer == -1 and your == 1:
        print("You Win!")
    elif computer == -1 and your == 0:
        print("You Lose!")
    elif computer == 1 and your == -1:
        print("You Lose!")
    elif computer == 1 and your == 0:
        print("You Win!")
    elif computer == 0 and your == -1:
        print("You Win!")
    elif computer == 0 and your == 1:
        print("You Lose!")
    else:
        print("Something went wrong")
        