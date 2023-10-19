import tkinter as tk
import random

user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    emojis = {
        "Rock": "✊",
        "Paper": "✋",
        "Scissors": "✌️",
    }

    user_emoji = emojis[user_choice]
    computer_emoji = emojis[computer_choice]

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Scissors" and computer_choice == "Paper")
        or (user_choice == "Paper" and computer_choice == "Rock")
    ):
        user_score += 1
        result = f"You win! {user_emoji} vs. {computer_emoji}"
    else:
        computer_score += 1
        result = f"Computer wins! {computer_emoji} vs. {user_emoji}"

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    result_label.config(text=result)

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    result_label.config(text="")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

root.geometry("400x400")

user_score_label = tk.Label(root, text="Your Score: 0", font=("Arial", 20))
user_score_label.pack()
computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 20))
computer_score_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.pack()

button_style = {"font": ("Arial", 20), "width": 10, "height": 2}

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"), **button_style)
paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"), **button_style)
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"), **button_style)
play_again_button = tk.Button(root, text="Play Again", command=reset_game, **button_style)

rock_button.pack(pady=20)
paper_button.pack(pady=20)
scissors_button.pack(pady=20)
play_again_button.pack(pady=20)

root.mainloop()
