import random
board=[" "]*9 # creating empty list to hold x and o
play=True

# function to print in order
def print_board(board):
    row1=" {} | {} | {}".format(board[0],board[1],board[2])
    row2="{} | {} | {}".format(board[3],board[4],board[5])
    row3="{} | {} | {}".format(board[6],board[7],board[8])
    print(row1,'\n',row2,'\n',row3)
    
def user_choice(board,user): # function to set move
    user_1=int(input("enter position  : "))-1
    if board[user_1]!=" ":
        print("already taken.. choose another!")
        user_choice(board,user)
    else:
        board[user_1]=user
        print_board(board)

def computer(board,user): # function for computer
    pos=random.randint(1,9)-1
    if board[pos]!=" ":
        computer(board,user)
    else:
        board[pos]=user
        print("Move by computer")
        print_board(board)

        
def win_check(board,u):  # win check
    
    if board[0]==u and board[1]==u and board[2]== u or board[3]==u and board[4]==u and board[5]==u or board[6]==u and board[7]==u and board[8]==u or board[0]==u and board[3]==u and board[6]==u or board[1]==u and board[4]==u and board[7]==u or board[2]==u and board[5]==u and board[8]==u or board[0]==u and board[4]==u and board[8]==u or board[2]==u and board[4]==u and board[6]==u :
        return False,u
    else:
        return True,None
print("\n\n..................................TIC   TAC   TOE........................................\n\n")
print("enter 1-9 for x and o positions")
opponent=input("enter yes if u want to play with computer: ")
u1=input('user1  choose your letter : ')
if u1=='x':
    u2='o'
else:
    u2='x'
while play :
    user_choice(board,u1)
    play,win=win_check(board,u1)
    if play==False:
        continue
    if opponent=='yes':
        computer(board,u2)
        play,win=win_check(board,u2)
        win='c'
    else:
        user_choice(board,u2)
        play,win=win_check(board,u2)


print("........Game Over .......")
print("\n")
if u1=='x' and win =='x' or u1=='o' and win=='o':
    print("User 1 wins")
elif win=='c':
    print("computer wins")
else:
    print("user 2 wins")
print("\n \n ........................................................................................................................\n\n")
