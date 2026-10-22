#Rachchh Visva
#92600584074

def display(board):
    print()
    print(board[0],"|",board[1],"|",board[2])
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])
    print()


def heuristic(board):
    win=[(0,1,2),
         (3,4,5),
         (6,7,8),
         (0,3,6),
         (1,4,7),
         (2,5,8),
         (0,4,8),
         (2,4,6)]

    for a,b,c in win:
        if board[a]==board[b]==board[c]=="x":
            return 100
        elif board[a]==board[b]==board[c]=="0":
            return -100

    return 0

board= [" "]*9
player="x"

for turn in range(9):
    display(board)
    print("player",player)

    position=int(input("enter position (1-9):"))-1

    if position<0 or position>8 or board[position] != " ":
        print("invalid!Try again")
        continue
    board[position]=player

    score = heuristic(board)

    if score == 100:
        display(board)
        print("player x wins")
        break

    if score == -100:
        display(board)
        print("player 0 wins")
        break

    if player == "x":
        player="o"

    else:player = "x"

else:
    display(board)
    print("Game Draw")
