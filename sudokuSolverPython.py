


def checkRow(sudoku, x, row):
    row1 = sudoku[row]
    #print(row1)
    if x in row1:
        return True
    else:
        return False

def checkCol(sudoku, x, row, col):

    i=0
    col1 = []
    for i in range(9):
        col1.append(sudoku[i][col])

    #print(col1)
    if x in col1:
        return True
    else:
        return False

def checkGrid(sudoku, x, row, col):
    rowBlock = (row//3)*3
    colBlock = (col//3)*3
    #print(rowBlock, colBlock)
    i = rowBlock+3
    j = colBlock+3
    for rowBlock1 in range(rowBlock,i):
        #print("rowBlock1: ",rowBlock1)
        for colBlock1 in range(colBlock,j):
            #print("colBlock1: ",colBlock1)
            if x == sudoku[rowBlock1][colBlock1]:
                #print("hit at",rowBlock1,colBlock1)
                #print("i= ",i," j= ",j)
                #print("values x: ",x)
                #printSudoku(sudoku)
                return True

    return False

def findEmptyCell(sudoku, empty_cell):
    #i,j = 0,0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                empty_cell[0] = i
                empty_cell[1] = j
                return True
    return False

def printSudoku(sudoku):
    i,j = 0,0
    for i in range(9):
        k = 0
        if(i%3 == 0 and i!=0):
            for k in range(21):
                print("-",end="")
            print()
        for j in range(9):
            if j%3 == 0 and j!=0:
                print('|',end=" ")
            print(sudoku[i][j],end=" ")
        print()


def ifValid(sudoku, num1, row, col):
    if  ( not checkRow(sudoku,num1,row) and not checkCol(sudoku,num1,row,col) and not checkGrid(sudoku,num1,row,col)):
        return True
    return False


def solve(sudoku):
    #printSudoku(sudoku)
    #print()
    empty_cell = [0,0]
    i,j = 0,0
    if (findEmptyCell(sudoku,empty_cell) == False):
        return True
    row = empty_cell[0]
    col = empty_cell[1]
    num1 = 1
    for num1 in range(1,10):

        if  (ifValid(sudoku,num1,row,col)):
            #print(checkRow(sudoku,num1,row), checkCol(sudoku,num1,row,col), checkGrid(sudoku,num1,row,col))
            sudoku[row][col] = num1

            #we go deeper and check next values
            if (solve(sudoku) == True):
                return True

            else:
                sudoku[row][col] = 0

    #BACKTRACKER
    return False





sudoku = [[3,1,6,5,0,8,4,0,0],
        [5,2,0,0,0,0,0,0,0],
        [0,8,7,0,0,0,0,3,1],
        [0,0,3,0,1,0,0,8,0],
        [9,0,0,8,6,3,0,0,5],
        [0,5,0,0,9,0,6,0,0],
        [1,3,0,0,0,0,2,5,0],
        [0,0,0,0,0,0,0,7,4],
        [0,0,5,2,0,6,3,0,0]]


#print(checkRow(sudoku, 1, 1))
#print(checkCol(sudoku, 1, 1, 2))
#print(checkGrid(sudoku, 1, 1, 2))
if (solve(sudoku)):
    printSudoku(sudoku)
else:
    print("No Solution")

#row,col = 0,0
