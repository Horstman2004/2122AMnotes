'''
    Goal of this program is to check and see if the Sudoku puzzle the user enters is correct.
    This program should be ran in the same directory as a text file called Puzzle.txt
    The program will check if the Sudoku puzzle is correct then output to the console if it is correct or not.
    If you've never played Sudoku before, here's the rules:  https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/
    I have listed out a couple ideas to create this program.  You do not need to do this my way, but I'm telling ya, it will help in the long run.
'''

filename="VerticalIssue.txt"
count = 0
#read in the text file into a 2D List so you can iterate through it like we did in Tic Tac Toe
#open the file
sudoku = open(filename,"r")
#utilize a for loop to iterate through the file
puzzleFromFile = list(sudoku)

    #each line should be converted into a list and appended to the board

 
#utilize a function where you enter a list or row and check if the row has 1-9 exclusively
def rowChecker(rowToCheck):
    #if the board isn't solved horizontally, then return False
    return True

'''
#create a function that takes in your 2D List above and checks if each horizontal row has 1-9 exclusively
def horizontalCheck(boardToCheck):
    #loop through the boardToCheck (which should be the puzzleFromFile variable)
    #   each iteration you will have a list so check to see if that list has 1-9, if it doesn't return False
    #if the board isn't solved horizontally, then return False
    return True

#create a function that takes in your 2D List above and checks if each vertical column has 1-9 exclusively
def verticalCheck(boardToCheck):
    #You should already have a function to check a row if it has 1-9 exclusively.
    #   Rotate the boardToCheck and pass in the board to horizontalCheck
    #if the board isn't solved horizontally, then return False
    return True

#create a function checks the different sections of board.  You could make the function dynamic by passing in which section to check.
def sectionCheck(boardToCheck):
    #if the board isn't solved horizontally, then return False
    return True

#working code
if horizontalCheck(puzzleFromFile):
    print("passed horizontally")
elif verticalCheck(puzzleFromFile):
    print("passed vertically")
elif sectionCheck(puzzleFromFile):    

        need to be able to tell the user which section failed
        there are 9 sections 
        1   2   3
        4   5   6
        7   8   9
    failedSection=1
    print(f"Section {failedSection} Didn't Pass")
    
    

    - You can assume the data coming in is like the examples
    - Need to tell the user where it failed, the more specific the more points (which row, which col, which section)
        - Some Points: tell the user which method failed first
        - Average Points: tell which row or column the puzzle failed on
        - All Points: the exact cell that failed
    - Seriously, you will want this for later.
    - Take baby steps.  That's why I recommend functions so you can get more points faster and partial credit when you're stuck.


'''


