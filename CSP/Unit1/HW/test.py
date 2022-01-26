board = [] #List for holding the board

for x in range(6):
    board.append(["_"] * 7) #builds 7 x 6 board (rows x columns)

#function for printing the board
def print_board(board):  
    for row in board:
        print(" ".join(row))
        
print_board(board)
