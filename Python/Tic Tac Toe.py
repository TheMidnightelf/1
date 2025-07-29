#Functions
def fun(board1):
    for i in range (3):
        print(board1[i])
# Initialize The Board
board = []
for i in range (3):
    temp = []
    for j in range(3):
        temp.append("-")
    board.append(temp)
for i in range (3):
    print(board[i])
# Get Player Input -> Print on Board
x = True
player = "0"
count = 1
while x:
    print(count)
    row = int(input("Row: "))
    col = int(input("Column: "))
    space = board[row-1][col-1]
    if space != "-":
        print("That space is taken!")
        count = count - 1
    else:
        board[row-1][col-1] = player
    fun(board)
# Check for Wins
# Horizontal
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][2] == board[i][1] and board[i][0] == player:
            print(player + "'s Win!")
            x = False
# Vertical
    for i in range(3):
        if board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[0][i] == player:
            print(player + "'s Win!")
            x = False
#Diagonal
    if board[0][0] == board[1][1] and board[2][2] == board[1][1] == board[0][0] == player:
        print(player + "'s Win!")
        x = False
    if board[0][2] == board[1][2] and board[2][0] == board[1][2] == board[0][2] == player:
        print(player + "'s Win!")
        x = False
# Swap Players
    count = count + 1
    if count % 2 == 0:
        player = "x"
    else:
        player = "0"