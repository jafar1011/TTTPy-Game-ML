import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("🎮 Tic Tac Toe vs Smart Bot")
root.config(bg="#1e1e2f")
root.geometry("600x680")

current_player = "X"
board = [""] * 9

def handle_click(index):
    if board[index] == "" and not check_winner(board):
        make_move(index, "X")
        if not check_winner(board) and "" in board:
            root.after(300, bot_move)

def make_move(index, player):
    board[index] = player
    buttons[index].config(text=player, disabledforeground="#fff")
    buttons[index]["state"] = "disabled"

    winner = check_winner(board)
    if winner:
        messagebox.showinfo("Game Over", f"{winner} wins!")
        disable_all()
    elif "" not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        disable_all()

def bot_move():
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    if best_move is not None:
        make_move(best_move, "O")

def minimax(state, depth, is_max):
    winner = check_winner(state)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif "" not in state:
        return 0

    if is_max:
        best = -float("inf")
        for i in range(9):
            if state[i] == "":
                state[i] = "O"
                best = max(best, minimax(state, depth + 1, False))
                state[i] = ""
        return best
    else:
        best = float("inf")
        for i in range(9):
            if state[i] == "":
                state[i] = "X"
                best = min(best, minimax(state, depth + 1, True))
                state[i] = ""
        return best

def check_winner(state):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if state[a] == state[b] == state[c] and state[a] != "":
            return state[a]
    return None

def disable_all():
    for btn in buttons:
        btn["state"] = "disabled"

def reset_board():
    global board
    board = [""] * 9
    for btn in buttons:
        btn.config(text="", state="normal")

title_label = tk.Label(
    root,
    text="Tic Tac Toe vs Bot",
    font=("Arial Black", 26),
    bg="#1e1e2f",
    fg="#00ffcc"
)
title_label.pack(pady=20)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

buttons = []
for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 32, "bold"),
        width=5,
        height=2,
        bg="#282c34",
        fg="#ffffff",
        activebackground="#3b3f4c",
        relief="ridge",
        bd=5,
        command=lambda i=i: handle_click(i)
    )
    btn.grid(row=i//3, column=i%3, padx=10, pady=10)
    buttons.append(btn)

reset_btn = tk.Button(
    root,
    text="🔄 Restart Game",
    font=("Arial", 16, "bold"),
    bg="#00ffcc",
    fg="#000",
    activebackground="#00ccaa",
    relief="ridge",
    bd=4,
    command=reset_board
)
reset_btn.pack(pady=20)
root.mainloop()
