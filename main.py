import random
import tkinter as tk
from tkinter import messagebox

choices = ["Snake", "Water", "Gun"]


def play_game():
    user_input = user_choice_var.get()
    comp_sel = random.choice(choices)

    result = determine_winner(user_input, comp_sel)

    messagebox.showinfo("Result", f"You chose {user_input}, computer chose {comp_sel}.\n\n{result}")

    if result == "user":
        user_score_var.set(user_score_var.get() + 1)
    elif result == "computer":
        computer_score_var.set(computer_score_var.get() + 1)

    round_number_var.set(round_number_var.get() + 1)

    if user_score_var.get() >= game_over_score:
        messagebox.showinfo("Game Over", "Congratulations! You won the game!")
        reset_game()
    elif computer_score_var.get() >= game_over_score:
        messagebox.showinfo("Game Over", "Sorry, the computer won the game. Better luck next time!")
        reset_game()


def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a draw!"
    if (user_choice == "Snake" and comp_choice == "Water") or \
            (user_choice == "Water" and comp_choice == "Gun") or \
            (user_choice == "Gun" and comp_choice == "Snake"):
        return "You win this round!"
    else:
        return "Computer wins this round!"


def reset_game():
    global user_score, computer_score, round_number
    user_score = 0
    computer_score = 0
    round_number = 1
    user_score_var.set(user_score)
    computer_score_var.set(computer_score)
    round_number_var.set(round_number)


user_score = 0
computer_score = 0
round_number = 1
game_over_score = 5

window = tk.Tk()
window.title("Snake-Water-Gun Game")

user_choice_var = tk.StringVar()
user_choice_var.set(choices[0])

user_score_var = tk.IntVar()
user_score_var.set(user_score)

computer_score_var = tk.IntVar()
computer_score_var.set(computer_score)

round_number_var = tk.IntVar()
round_number_var.set(round_number)

choice_label = tk.Label(window, text="Choose: Snake, Water, Gun")
choice_label.pack()

choice_menu = tk.OptionMenu(window, user_choice_var, *choices)
choice_menu.pack()

play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()

score_label = tk.Label(window, text="Score:")
score_label.pack()

user_score_label = tk.Label(window, textvariable=user_score_var)
user_score_label.pack()

computer_score_label = tk.Label(window, textvariable=computer_score_var)
computer_score_label.pack()

round_label = tk.Label(window, text="Round:")
round_label.pack()

round_number_label = tk.Label(window, textvariable=round_number_var)
round_number_label.pack()

reset_button = tk.Button(window, text="Reset", command=reset_game)
reset_button.pack()

exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.pack()

window.mainloop()
