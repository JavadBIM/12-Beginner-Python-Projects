import random

# Just published On GIT

user_choice = input("What is Your Choice ?[R] for Rock , [P] for Paper , [S] for scissors: \n")
pc_choice = random.choice(["R", "P", "S"])


# Defining the win situation
def is_win():
    if user_choice == "R" and pc_choice == "S" or user_choice == "P" and pc_choice == "R" or user_choice == "S" and \
            pc_choice == "S":
        return True


# Actual Game
def rpc():
    if user_choice == pc_choice:
        print("Play Again , it was a tie")
    # r>s p>r s>p
    elif is_win():
        print("You Just Won")
    else:
        print("You Lose !")


print(pc_choice)
rpc()
