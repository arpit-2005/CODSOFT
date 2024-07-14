import random

def play_game():
    
    
    print("Welcome to the Game")
    print("choose one from  Rock, Paper, Scissor")
    
    # user's choice
    user_choice = input("your choice: ").lower()
    if user_choice not in ['rock','paper','scissor']:
        print("invalid choice\n1. choose from rock, paper, scissor\n2. Enter the correct spelling")
        return
    
    # computer's choice
    computer_choice = random.choice(['rock','paper','scissor'])
    print(f"computer choice: {computer_choice}")

    #building the logic
    if (user_choice == computer_choice):
         result = 'tie'
         
    elif (user_choice == 'rock' and computer_choice == 'scissor')or(user_choice == 'paper' and computer_choice == 'rock')or(user_choice == 'scissor' and computer_choice == 'paper'):
          result = 'win'
          
    else:
          result = 'lose'
          
    
    # declaring who wins the round
    if (result == 'tie'):
         print("Its a tie!") 
    elif (result == 'win'):
         print("you won!")
    else:
         print("you lose!")     

          
     

    #asking the user if he/she wants to play again or not
    play_again =  input("Do you want to play again, Answer in (Yes,No):").lower()
    if play_again == 'yes':
          play_game()
    else:
         print("Thanks for Playing the game!")

play_game()

        
    

