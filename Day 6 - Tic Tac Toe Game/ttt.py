import numpy as np

# Create an empty 3x3 matrix to represent the Tic Tac Toe board
m = np.zeros((3, 3), dtype=str)

# Making Empty Matrix
def makeEmptyMatrix():
    for i in range(0, 3):
        for j in range(0, 3):
            m[i, j] = '_'

# Changing the value at coordinates
def player1():
    # Inputting the position coordinates
    pinstr = input("Player 1 (O): Enter the position you want to mark as xy : ")
    px = int(pinstr[0])
    py = int(pinstr[1])
    
    m[px, py] = 'O'
    print(m)

def player2():
    # Inputting the position coordinates
    pinstr = input("Player 2 (X): Enter the position you want to mark as xy : ")
    px = int(pinstr[0])
    py = int(pinstr[1])
    
    m[px, py] = 'X'
    print(m)

def check_rows():
    for i in range(3):
        if m[i, 0] == m[i, 1] == m[i, 2] != '_':
            return True
    return False

def check_columns():
    for i in range(3):
        if m[0, i] == m[1, i] == m[2, i] != '_':
            return True
    return False

def check_diagonals():
    if m[0, 0] == m[1, 1] == m[2, 2] != '_':
        return True
    if m[0, 2] == m[1, 1] == m[2, 0] != '_':
        return True
    return False

def wincheck():
    return check_rows() or check_columns() or check_diagonals()

# The Game
makeEmptyMatrix()
print("Initial Board:")
print(m)

for i in range(0, 9):
    if i % 2 == 0:
        player1()
        if wincheck():
            print("Player 1 (O) wins!")
            break
    else:
        player2()
        if wincheck():
            print("Player 2 (X) wins!")
            break

print("Game Over")
