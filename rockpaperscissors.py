import random
#print('Computer: 🪨  vs  ✂️ : User')
list_game=["rock","paper","scissors"]
computer_selection_random= ""
user_count= 0
computer_count=0
user_play=''
game_iteration= 0

def menu():
    print(f"\n\n*************************ROCK-PAPER-SCISSORS************************* \n")

    
def menu_ingame():
    print(f'                              Pick an option:\n')
    print(f'                      Rock✊   Paper✋   Scissors⚔\n')



menu()
while game_iteration <3 and user_count < 2 and computer_count < 2:
    
    computer_selection_random=list_game[random.randrange(0,3)]
    menu_ingame()
    user_selection= input('Choose an option?: ').lower().strip()
    
    if user_selection not in list_game:
        print(f"\n Choose one of the valid options \n")
        continue

    else:   
        game_iteration += 1
        print(f"\n Try {game_iteration}/3")
        print(f"\n-----------> You: {user_selection.upper()}  VS  {computer_selection_random.upper()} :Computer <----------- \n")

    # Bloque ROCK

        if user_selection == 'rock' and computer_selection_random == 'rock':
            print('It is a draw!!!! \n') 
            print(f"                        SCORE \n")
            print(f'                       YOU: {user_count}')
            print(f"                       COMPUTER: {computer_count} ")
            continue

        if user_selection == 'rock' and computer_selection_random == 'paper':
            computer_count += 1
            print(f"                        SCORE \n")
            print(f'                       YOU: {user_count}')
            print(f"                       COMPUTER: {computer_count} ")

        if user_selection == 'rock' and computer_selection_random == 'scissors':
            user_count += 1
            print(f"                        SCORE \n")
            print(f'                       YOU: {user_count}')
            print(f"                       COMPUTER: {computer_count} ")

    # Bloque PAPER  
        
        if user_selection == 'paper' and computer_selection_random == 'paper':
            print('It is a draw!!!! \n') 
            print(f"                        SCORE \n")
            print(f'                       YOU: {user_count} ')
            print(f"                       COMPUTER: {computer_count} ")
            continue

        if user_selection == 'paper' and computer_selection_random == 'rock':
            user_count += 1
            print(f"                        SCORE \n")
            print(f'                       YOU: {user_count}')
            print(f"                       COMPUTER: {computer_count} ")

        if user_selection == 'paper' and computer_selection_random == 'scissors':
            computer_count += 1
            print(f"                        SCORE \n")
            print(f'                       YOU: {user_count}')
            print(f"                       COMPUTER: {computer_count} ")
        
    # Bloque SCISSORS

        if user_selection == 'scissors' and computer_selection_random == 'scissors':
            print('It is a draw!!!! \n') 
            print(f"                        SCORE \n")
            print(f'                       YOU: {user_count} ')
            print(f"                       COMPUTER: {computer_count} ")
            continue

        if user_selection == 'scissors' and computer_selection_random == 'rock':
            print(f"                        SCORE \n")
            print(f'                       YOU: {user_count}')
            print(f"                       COMPUTER: {computer_count} ")

        if user_selection == 'scissors' and computer_selection_random == 'paper':
            user_count += 1
            print(f"                        SCORE \n")
            print(f'                       YOU: {user_count}')
            print(f"                       COMPUTER: {computer_count} ")
    

if user_count == 2 or user_count > computer_count:
    print(f'\n\n                        You WIN!!!!')

elif computer_count == 2 or user_count < computer_count:
    print(f'\n\n                        Computer WINS!!!!')
else:
    print(f'\n\n                        It is a draw')
    
    
