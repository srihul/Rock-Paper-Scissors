from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Rock Paper Scissor Game")

computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player ")
    l3.config(text="Computer")
    l4.config(text="")
    computer_label.config(text="")

def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

def isrock():
    player_choice = "Rock"
    computer_choice = computer_value[str(random.randint(0, 2))]
    display_result(player_choice, computer_choice)

def ispaper():
    player_choice = "Paper"
    computer_choice = computer_value[str(random.randint(0, 2))]
    display_result(player_choice, computer_choice)

def isscissor():
    player_choice = "Scissor"
    computer_choice = computer_value[str(random.randint(0, 2))]
    display_result(player_choice, computer_choice)

def display_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        match_result = "Match Draw"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissor") or
        (player_choice == "Scissor" and computer_choice == "Paper") or
        (player_choice == "Paper" and computer_choice == "Rock")
    ):
        match_result = "Player Win"
    else:
        match_result = "Computer Win"

    l4.config(text=f"Player: {player_choice}\nComputer: {computer_choice}\nResult: {match_result}")
    button_disable()

Label(root, text="Rock Paper Scissor", font="normal 20 bold", fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame, text="Player ", font=10)
l2 = Label(frame, text="VS ", font="normal 10 bold")
l3 = Label(frame, text="Computer", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root, text="", font="normal 20 bold", bg="white", width=25, borderwidth=2, relief="solid")
l4.pack(pady=20)

computer_label = Label(root, text="", font="normal 12")
computer_label.pack()

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock", font=10, width=7, command=isrock)
b2 = Button(frame1, text="Paper", font=10, width=7, command=ispaper)
b3 = Button(frame1, text="Scissor", font=10, width=7, command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Reset Game", font=10, fg="red", bg="black", command=reset_game).pack(pady=20)

root.mainloop()
