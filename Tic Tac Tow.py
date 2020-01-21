# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:36:36 2020

@author: richa
"""

def main():
    
    board = [' ']*10
    
    print('Welcome to Tic Tac Tow')
    check_full(board)
    player_marker(board)
    #create_board(board,player1)
    
    
    
        

def create_board(board,player1):
        
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    
    
def player_marker(board):
    
    marker = ' '
    player1 = ' '
    player2 = ' '
    while marker != 'X' and marker != 'O':
       marker = input('Player 1 choose you marker X or O: ').upper()

       
       if marker == 'X':
           player1 = marker
           player2 = 'O'
       else:
           player1 = marker
           player2 = 'X'
    
    print(f'\nPlayer1 is {player1} and Player2 is {player2}')
    
    while check_full(board)==False or win_check(board,player1,player2)==False:
        # win_check(board,player1,player2)==False:

            if win_check(board,player1,player2) == True:
            
                print('done')
                break
            else:
                input_position_player1(board,player1)
        
    
                input_position_player2(board,player2)
    

           
    

def input_position_player1(board,player1):

        
    position1  = int(input('Player1 enter the position where you would like to place your marker: '))
        
    board[position1] = player1
        
    create_board(board,player1)
  
def input_position_player2(board,player2):
        
    position2  = int(input('Player2 enter the position where you would like to place your marker: '))
        
    board[position2] = player2
        
    create_board(board,player2)

            
def check_full(board):
    
   for i in board:
       if ' 'in i:
           return False
       else:
           return True


def win_check(board,player1,player2):
    
    return ((board[7] == (player1 or player2) and board[8] == (player1 or player2) and board[9] == (player1 or player2)) or # across the top
    (board[4] == (player1 or player2) and board[5] == (player1 or player2) and board[6] == (player1 or player2)) or # across the middle
    (board[1] == (player1 or player2) and board[2] == (player1 or player2) and board[3] == (player1 or player2)) or # across the bottom
    (board[7] == (player1 or player2) and board[4] == (player1 or player2) and board[1] == (player1 or player2)) or # down the middle
    (board[8] == (player1 or player2) and board[5] == (player1 or player2) and board[2] == (player1 or player2)) or # down the middle
    (board[9] == (player1 or player2) and board[6] == (player1 or player2) and board[3] == (player1 or player2)) or # down the right side
    (board[7] == (player1 or player2) and board[5] == (player1 or player2) and board[3] == (player1 or player2)) or # diagonal
    (board[9] == (player1 or player2) and board[5] == (player1 or player2) and board[1] == (player1 or player2))) # diagonal


        
    
main()