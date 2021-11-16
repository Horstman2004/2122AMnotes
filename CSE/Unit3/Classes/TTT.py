b="""
    |   |   
-------------
    |   |   
-------------
    |   |   
    
"""
board=[[" "," "," "],[" "," "," "],[" "," "," "]]
board[1][1]     #access the middle cell
sampleboard=[[1,2,3],[4,5,6],[7,8,9]]
'''
print(sampleboard)
for row in range(len(sampleboard)):    #range(len(sampleboard)) -> [0,1,2]
    for columns in range(len(sampleboard[row])):
        print(sampleboard[row][columns])
'''

def printboard(board):      
    for r in range(3):
        print(board[r][0]+" |"+board[r][1]+" | "+board[r][2])
        if r<2:
            print("-"*8)

def choosespot(r,c,symbol,board)
    if board[r][c] = " ":
        board[r][c]=symbol
        return True
    return Fasle

printboard(board)

r = int(imput("row: "))-1
c = int(input("col: "))-1
board[r][c]="x"
printboard(board)
r = int(imput("row: "))-1
c = int(input("col: "))-1
board[r][c]="o"


while symbol!="Q"
    printboard(board)
    
    goodspot=False
    while not goodspot:
      1
      1
      1
      1
      1
      11
    
    
    
    
    
    
    
    #check for a winner or CAT
    if catgame(board):
        symbol="Q"
    #switching our symbols
    if symbol=="x"
        symbol="o"
    elif symbol=="o":
        symbol="x"      
        
        #check vertically 
        
        #check diagonally
        #hardcode