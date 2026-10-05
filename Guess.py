import random
am_guesses = 0
max_range = 5
#Random range depending on difficulty
#diff_part = input() 
diff_wheel = input("Which Difficulty Would You Like? Easy, Medium, Hard, Extreme, Infinity")
print("Easy is 1 to 5, Medium is 1 to 10, Hard is 1 to 100, Extreme is 1 to 1,000, and infinity is 1 to 10 Million. ")
if diff_wheel.lower() == "easy":
        max_range = 5
elif diff_wheel.lower() == "medium":
        max_range = 10
elif diff_wheel.lower() == "hard":
        max_range = 100
elif diff_wheel.lower() == "extreme":
        max_range = 1000
elif diff_wheel.lower() == "infinity":
        max_range = 10000000
num1 = random.randint(1, max_range)
guess_lim = 10
while True:
    guess = input("Enter A number :)")
    guess = int(guess)
    guess_lim -= 1
    if guess_lim == 0:
        print("You Ran Out Of Guesses!")
        break
    if num1 > guess:
        print("Your Number Needs to be Higher!")
        am_guesses += 1
    elif num1 < guess:
        print("Your Number Needs to be Lower!")
        am_guesses += 1

    elif num1 == guess:
        print("Correct!")
        am_guesses +=1
        print("You Took a total of " + str(am_guesses) + " guesses!")
        break
