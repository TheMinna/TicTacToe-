import os
import random
import time

def clear():
    print("")
    input("[Press Enter] ")
    os.system('cls')

def clear_without_enter():
    print("")
    os.system('cls')

def grid():
    print(f'''
     {moves_dict['t1']} | {moves_dict['t2']} | {moves_dict['t3']}
    -----------
     {moves_dict['m1']} | {moves_dict['m2']} | {moves_dict['m3']}
    -----------
     {moves_dict['b1']} | {moves_dict['b2']} | {moves_dict['b3']}
    ''')
    print("")

def make_move(move, symbol):
    err = " "
    if move.isdigit():
        if int(move) > 9 or int(move) < 1 or move == "":
            err = "Choose a place from the grid [1-9]: "
            return 0, err
        elif move == "1":
            if moves_dict['t1'] == " ":
                moves_dict['t1'] = symbol
                return -1, err
            else: 
                err = "Nope, that place already has a symbol."
                return 0, err 
        elif move == "2":
            if moves_dict['t2'] == " ":
                moves_dict['t2'] = symbol
                return -1, err
            else: 
                err = "Nope, that place already has a symbol."
                return 0, err 
        elif move == "3":
            if moves_dict['t3'] == " ":
                moves_dict['t3'] = symbol
                return -1, err
            else: 
                err = "Nope, that place already has a symbol."
                return 0, err 
        elif move == "4":
            if moves_dict['m1'] == " ":
                moves_dict['m1'] = symbol
                return -1, err
            else: 
                err = "Nope, that place already has a symbol."
                return 0, err 
        elif move == "5":
            if moves_dict['m2'] == " ":
                moves_dict['m2'] = symbol
                return -1, err
            else: 
                err = "Nope, that place already has a symbol."
                return 0, err 
        elif move == "6":
            if moves_dict['m3'] == " ":
                moves_dict['m3'] = symbol
                return -1, err
            else: 
                err = "Nope, that place already has a symbol."
                return 0, err 
        elif move == "7":
            if moves_dict['b1'] == " ":
                moves_dict['b1'] = symbol
                return -1, err
            else: 
                err = "Nope, that place already has a symbol."
                return 0, err  
        elif move == "8":
            if moves_dict['b2'] == " ":
                moves_dict['b2'] = symbol
                return -1, err
            else: 
                err = "Nope, that place already has a symbol."
                return 0, err 
        elif move == "9":
            if moves_dict['b3'] == " ":
                moves_dict['b3'] = symbol
                return -1, err
            else: 
                err = "Nope, that place already has a symbol."
                return 0, err 
    else:
        err = "Please choose a number [1-9]: "
        return 0, err 
    

def check_result(symbol):
    print("Game Over")
    if (symbol == moves_dict['t1'] == moves_dict['t2'] == moves_dict['t3']) or (symbol == moves_dict['m1'] == moves_dict['m2'] == moves_dict['m3']) or (symbol == moves_dict['b1'] == moves_dict['b2'] == moves_dict['b3']) or (symbol == moves_dict['t1'] == moves_dict['m1'] == moves_dict['b1']) or (symbol == moves_dict['t2'] == moves_dict['m2'] == moves_dict['b2']) or (symbol == moves_dict['t3'] == moves_dict['m3'] == moves_dict['b3']) or (symbol == moves_dict['t1'] == moves_dict['m2'] == moves_dict['b3']) or (symbol == moves_dict['t3'] == moves_dict['m2'] == moves_dict['b1']):
        return True
    else:
        return False
    

# ASCII Art made with https://www.asciiart.eu/text-to-ascii-art
def logo():
    print('''
    >>==================================================================<<
    ||                                                                  ||
    ||   _____  _   __       _____   __    __       _____  ___   ____   ||
    ||    | |  | | / /`       | |   / /\  / /`       | |  / / \ | |_    ||
    ||    |_|  |_| \_\_,      |_|  /_/--\ \_\_,      |_|  \_\_/ |_|__   ||
    ||                                                                  ||
    >>==================================================================<<
    ''')

logo()

opponent = ""
ai_opponent = False

while opponent != "1" and opponent != "2":
    opponent = input("Choose your opponent:\n[1] Human \n[2] Computer ")

# Get Player names:
if opponent == "1":
    print("")
    player1 = input("Name of Player 1? ")
    if player1 == "":
        player1 = "Player1"
    player2 = input("Name of Player 2? ")
    if player2 == "":
        player2 = "Player2"
else: 
    player1 = input("What's your name? ")
    player2 = "Computer"
    ai_opponent = True

os.system('cls')
logo()
if opponent == "1":
    print(f"Welcome {player1} and {player2}!")
else:
    print(f"Welcome {player1}!")



moves_dict = {"t1": " ", "t2": " ", "t3" : " ", 
              "m1": " ", "m2": " ", "m3": " ",
              "b1": " ", "b2": " ", "b3": " "
              }

symbol = " "
is_winner = False 

clear()
print("Here's your game grid.")

grid()

clear()

print("Here are the possible moves.")

print('''
     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
''')
print("")

clear()


game_on = True
turns = 9
err = " "


while game_on and turns > 0:
    print("Let's play!")
    print(f"{err}")
    if turns % 2 != 0:
        symbol = "X"
        player = player1
    else:
        symbol = "O"
        player = player2
    grid()
    print("")
    if ai_opponent and symbol == "O":
        comp_turn = True
        while comp_turn: 
            comp_random = random.randint(0, 8)  ## Computer chooses a random spot. This could be modified to look for two same symbols in a row and choose one's place accordingly.
            ai_choice = list(moves_dict)[comp_random]
            if moves_dict[ai_choice] == " ":
                print("Computer is Thinking...")
                time.sleep(random.randint(1, 4))
                moves_dict[ai_choice] = symbol
                turns -= 1
                comp_turn = False
        
    else:
        move = input(f"{player}'s Choice: ")
        counter, err = make_move(move, symbol)
        turns += counter
    clear_without_enter()
    is_winner = check_result(symbol)
    if is_winner:
        game_on = False
    

grid()
if is_winner and symbol == "X":
    print(f"{player1} won!")
elif is_winner and symbol == "O":
    print(f"{player2} won!")
else:
    print("Tie!")
    print("")
print("")
print("Thank you for playing!\nBye bye.")



