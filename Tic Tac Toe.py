import tkinter as tk
from tkinter import messagebox

# Check all winning combinations
def check_winner():
    wins = [(0,1,2), (3,4,5), (6,7,8),  # rows
            (0,3,6), (1,4,7), (2,5,8),  # columns
            (0,4,8), (2,4,6)]           # diagonals
    for i, j, k in wins:
        if b[i]['text'] == b[j]['text'] == b[k]['text'] != "":
            return b[i]['text']
    return None

# Handle button click
def click(i):
    if b[i]['text'] == "" and not game_over[0]:
        b[i]['text'] = turn[0]  # mark the move
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            game_over[0] = True
        elif all(btn['text'] != "" for btn in b):  # check draw
            messagebox.showinfo("Game Over", "It's a draw!")
            game_over[0] = True
        else:
            turn[0] = "O" if turn[0] == "X" else "X"  # switch turn

# Reset the game
def reset():
    for btn in b:
        btn['text'] = ""
    turn[0] = "X"
    game_over[0] = False

# Setup GUI
root = tk.Tk()
root.title("Tic Tac Toe")

turn = ["X"]        # current player
game_over = [False] # flag for game status

# Create 9 buttons for the board
b = [tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
               command=lambda i=i: click(i)) for i in range(9)]

# Arrange buttons in 3x3 grid
for i, btn in enumerate(b):
    btn.grid(row=i//3, column=i%3)

# Add reset button
tk.Button(root, text="Reset", font=("Arial", 14), 
          command=reset).grid(row=3, column=0, columnspan=3, sticky="we")

root.mainloop()