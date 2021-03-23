
import random

age = float(input("how old are? \t "))
upper_limit = 20g

if age > 10:
    upper_limit = 100

computer_number = random.randint(1,upper_limit)
print('The computer has selected a number between 1 and ' + str(upper_limit))
    
number_of_guesses = 0

def guess_check(selected_number, user_choice):
    if selected_number == user_choice:
        result = "win"
    elif selected_number > user_choice:
        result = "low"
    elif selected_number < user_choice:
        result = "high"
    return result

  
user_guess = int(input("what number do you think the computer selected? \t"))
number_of_guesses += 1

result_of_guess = guess_check(computer_number, user_guess)
while result_of_guess != "win" :
    if result_of_guess == "low":
      number_of_guesses += 1
      user_guess = int(input("Sorry, your guess is too low. Try again"))
    else:
      number_of_guesses += 1
      user_guess = int(input("Sorry, your guess is too high. Try again"))
        
    result_of_guess = guess_check(computer_number, user_guess)

print (f'Good job. You guessed right on {number_of_guesses} attempts')
        
