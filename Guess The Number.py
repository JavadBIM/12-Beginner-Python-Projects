
import random

def user_guess (x) :
    rand_int = random.randint(1, x)
    user_guess = 0
    while user_guess != rand_int :
        user_guess = int(input("Guess your number please: "))
        if user_guess > x :
            print("Unlucky it is higher!")
        elif user_guess < x :
            print("Unlucky it is lower!")


    print(f"Congratulation ! You guessed the right Number . {rand_int} is the right answer!")

user_guess(10)

def pc_guess (high) :
    feedback = ""
    while feedback  != "c":
        low = 0
        pc_answer = random.randint(low, high)
        feedback = input(f"if the {pc_answer} is high , type [H] if it is low type [L] , if it is correct, Type [C]").lower()
        if feedback == "l":
            low = low + 1
        elif feedback == "h" :
            high = high - 1
        print(pc_answer)
    print("Congratulation")

pc_guess(50)








