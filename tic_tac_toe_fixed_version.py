# -*- coding: utf-8 -*-
"""
Copied from github on Thu Dec 28 01:44:59 2023

@author: sunny4u from github
"""
#@@ -1,16 +1,13 @@
# tic tac toe
#tic tac toe
"""
[x]: draw a board
[x]: input player Name
[x]: put sign to each player
[x]: if they don't input between (1,9), direct them to previous state
[x]: if they don't input between (1,9), direct them to previous state 
[X]: put sign to exact spot
[X]: print board after each input
[x]: calculate and show result
"""

import sys

instructions = """
The tic tac toe board will be displayed alongside the numbers to show the \
position you would desire to input your symbol.       
Player 1 will go first.
"""

sign_dict = [[] for x in range(9)]

def print_start_board():
    board = f"""
     1 | 2 | 3
    ---|---|---
     4 | 5 | 6
    ---|---|---
     7 | 8 | 9
      """
    print(board)
def print_board(sign_dict):
    board = f"""
     {sign_dict[0][0]} | {sign_dict[1][0]} | {sign_dict[2][0]}
    ---|---|---
     {sign_dict[3][0]} | {sign_dict[4][0]} | {sign_dict[5][0]}
    ---|---|---
     {sign_dict[6][0]} | {sign_dict[7][0]} | {sign_dict[8][0]}
    """
    print(board,end='')
    print_start_board()

index_list = [None] * 9


def take_input(player_name):
    """checks whether number is already inserted"""
    c=0
    while c == 0:
        c += 1    
        x = int(input(f"Enter the position you would like to insert your \
symbol,'{player_name}':\n"))
        x -= 1
        if 0 <= x < 10:
            if index_list[x] != None:
                print('This spot is blocked.')
                c = 0
                continue
            else:
                index_list[x]=1
                c = 1
    return x

def result_calculation(player_one, player_two):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for condition in win_conditions:
            if sign_dict[condition[0]][0] == sign_dict[condition[1]][0] == sign_dict[condition[2]][0] != ' ':
                if sign_dict[condition[0]][0] == 'X':
                    print(f'Congratulations {player_one}. You WON!!!')
                else:
                    print(f'Congratulations {player_two}. You WON!!!')
                print('Thank you both for joining!')
                sys.exit()

        if all(sign_dict[i][0] != ' ' for i in range(9)):
            print("This is a tie!!! Nobody won. Please play again.")
            return False
    
def main():
    c=0
    print("Welcome to James' tic tac toe game!")
    player_one = input("Enter player 1 name:")
    player_two = input("Enter player 2 name:")
    print(f"Thank you for joining Mr./Mrs. {player_one} and Mr./Mrs. {player_two}.")
    print(instructions)
    print(f"{player_one}'s sign is: X")
    print(f"{player_two}'s sign is: O")
    while c==0:
        c=1
        input("Enter any key to start the game: ")
        print_start_board()
        for i in range(0, 9):
            if i % 2 == 0:
                index = take_input(player_one)
                sign_dict[index][0] = 'X'
            else:
                index = take_input(player_two)
                sign_dict[index][0] = 'O'
            print_board(sign_dict)
            result_calculation(player_one, player_two)
        print('The game has ended as a tie.')
        choice=int(input('Do you want to play again:\n\t1.Yes\n\t2.No\n'))
        if choice==1:
            index_list=[None] * 9
            c=0
        else:
            print('Thank you both for playing!')
 
main()

"""
This is my original result_calculation function.It is not executed.
def result_calculation(player_one, player_two): 
    if sign_dict[0][0] == sign_dict[1][0] == sign_dict[2][0] == 'X' or sign_dict[1][0] == sign_dict[4][0] == \
            sign_dict[7][0] == 'X' or sign_dict[0][0] == sign_dict[4][0] == sign_dict[8][0] == 'X' or sign_dict[2][0] == \
            sign_dict[5][0] == sign_dict[8][0] == 'X' or sign_dict[3][0] == sign_dict[4][0] == sign_dict[5][0] == 'X' or \
            sign_dict[2][0] == sign_dict[4][0] == sign_dict[6][0] == 'X' or sign_dict[6][0] == sign_dict[7][0] == \
            sign_dict[8][0] == 'X' or sign_dict[0][0] == sign_dict[3][0] == sign_dict[6][0] == 'X':
        print(f'Congratulations {player_one}. You WON.!!')
        sys.exit('Thank you both for joining')
    elif sign_dict[0][0] == sign_dict[1][0] == sign_dict[2][0] == 'O' or sign_dict[1][0] == sign_dict[4][0] == \
            sign_dict[7][0] == 'O' or sign_dict[0][0] == sign_dict[4][0] == sign_dict[8][0] == 'O' or sign_dict[2][0] == \
            sign_dict[5][0] == sign_dict[8][0] == 'O' or sign_dict[3][0] == sign_dict[4][0] == sign_dict[5][0] == 'O' or \
            sign_dict[2][0] == sign_dict[4][0] == sign_dict[6][0] == 'O' or sign_dict[6][0] == sign_dict[7][0] == \
            sign_dict[8][0] == 'O' or sign_dict[0][0] == sign_dict[3][0] == sign_dict[6][0] == 'O':
        print(f'Congratulations {player_two}. You WON.!!')
        sys.exit('Thank you both for joining')
    else:
        return False
"""