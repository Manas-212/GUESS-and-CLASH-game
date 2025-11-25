import random

lowest_num = 10
highest_num = 100
number = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("CAN YOU GUESS THE NUMBER?")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:
  guess = input("enter your guess:")

  if guess.isdigit():
    guess = int(guess)
    guesses += 1

    if guess < lowest_num or guess > highest_num:
      print("that number is out of range")
      print(f"select a number between {lowest_num} and {highest_num}")
    elif guess < number:
      print("too low!! try again!")
    elif guess > number:
      print("too high!! try again!")
    else:
      print(f"CORRECT!! the number was {number} ")
      print(f"total number of guesses : {guesses}")
      is_running = False
      print("you have won the 1st level. do you want to go to next level?")
      choice = input("yes or no:").lower()
      if choice == "no":
        print("THANKS FOR PLAYING!!")
        print("COME AGAIN.")
      if choice == "yes": 
        options = ("rock", "paper", "scissors")
        running = True
        while running:
          player = None
          computer = random.choice(options).lower()
          player = input("enter you choice('rock', 'paper','scissors'):").lower()
          while player not in options:
            print("INVALID GUESS")
            player = input("enter you choice('rock', 'paper','scissors'):").lower()
          print(f"player:{player}")      
          print(f"computer:{computer}")
          if player == computer:
            print("it's a tie")
          elif player == "scissors" and computer == "paper":
            print("YOU WON!!!")  
          elif player == "paper" and computer == "rock":
            print("YOU WON!!!")
          elif player == "rock" and computer == "scissor":
            print("YOU WON!!!")
          else:
                  print("YOU LOST!!!")
          play_again = input("do you wanna play again?(y/n)").lower()
          if play_again == "n":          
                  running = False
                  print("THANKS FOR PLAYING!!!")
                         
  else:
    print("INVALID GUESS")
    print(f"select a number between {lowest_num} and {highest_num}")