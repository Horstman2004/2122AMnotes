#UNFINISHED
#Varibles
filename="HorizontalIssue.txt"
rowcount = 0
total = 0
#open the file
with open(filename,"r") as f:
    board=f.readlines()
print(board)
for i in range(len(board)):
    board[i]=board[i].rstrip()
print(board)

"""
for i in sudoku:
    puzzle = list(i[0:9:1])
    #puzzle = [int(item) for item in puzzle]
    print(puzzle[0:9])
 
#utilize a function where you enter a list or row and check if the row has 1-9 exclusively
def rowChecker():
    for row in puzzle[0:3]:
        row = list(row)
        print(row)
    return True
rowChecker()
"""

def rowChecker(rowToCheck):
    temp=[]
    print(rowToCheck)
    for i in range(len(rowToCheck)):
        if rowToCheck[i] in temp:
            print(f"Failed at {i+1}")
            print(temp)
            return False
        else:
            temp.append(rowToCheck[i])

def horizontalCheck(boardToCheck):
    for i in range(len(board)):
        rowChecker(boardToCheck[i])


choser = input("What row do you want to check (rows,columns)?")
if choser == "rows":
    for j in range(9):
        rowChecker(board[j-1])
elif choser == "columns":
    index1 = 0
    index2 = 0
    columnList=[]
    for j in range(9):
        index2+=1
        for j in range(9):
            index1+=1
            temp=[board[index1:index2]]
            columnList.append(temp[0])
