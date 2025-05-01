# Pass this function a list of lists, and it will
# print it such that it looks like the grids in
# the exercise instructions.
def print_board(board):
    for i in range(len(board)):
        
        # This line uses some Python you haven't
        # learned yet. You'll learn about this
        # part in a future lesson:
        #
        # [str(x) for x in board[i]]
        print(" ".join([str(x) for x in board[i]]))

# Your code here...

my_grid = []# create a blank list to hold the grid

for i in range(8):# for loop 8 times
    my_grid.append([0]*8)# empty list elament zero times 8 haves it where theirs 8 rows of zeros

for row in range(8):#for loop 8 times varub
    for col in range(8):# for collom in range 8 times
        if(row + col) % 2 == 1 and (row < 3 or row > 4):# if row + colom modulus 2 is equal to one and row less than three and greater than four
            my_grid[row][col] = 1# replace with one
     
print_board(my_grid)


 # if(row + col) % 2 == 1:# if row + collom remander of 2 = 1
           # my_grid[row][col] = 1
