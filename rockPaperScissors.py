import random
list = ["Rock", "Paper", "Scissor"]
i, c, u, d = 0, 0, 0, 0
while (i < 3):
    user_choice = int(input("[0 - rock]\n[1 - paper]\n[2 - scissor]\nEnter your choice : "))
    if user_choice < 0 or user_choice > 2:
        print("Enter correct choice.")
    else:
        comp_choice = random.randint(0, 2)
        if (user_choice == comp_choice):
            print(f"You have chosen {list[user_choice]} and I have chosen {list[comp_choice]} so its a draw\n\n")
            d = d+1
        elif user_choice == 0 and comp_choice == 2:
            print(f"You have chosen {list[user_choice]} and I have chosen {list[comp_choice]} so you win\n\n")
            u = u+1
        elif user_choice == 2 and comp_choice == 0:
            print(f"You have chosen {list[user_choice]} and I have chosen {list[comp_choice]} so I win\n\n")
            c = c+1
        elif (user_choice > comp_choice):
            print(f"You have chosen {list[user_choice]} and I have chosen {list[comp_choice]} so you win\n\n")
            u = u+1
        elif (comp_choice > user_choice):
            print(f"You have chosen {list[user_choice]} and I have chosen {list[comp_choice]} so I win\n\n")
            c = c+1
        i = i+1