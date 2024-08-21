import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        return "Player"
    else:
        return "Computer"

# Function to handle button clicks
def on_button_click(player_choice):
    # Computer's choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    # Determine the result
    result = determine_winner(player_choice, computer_choice)
    
    # Display the result
    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\nYou chose: {player_choice}\nResult: {result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create buttons for Rock, Paper, Scissors
button_rock = tk.Button(root, text="Rock", command=lambda: on_button_click("Rock"))
button_paper = tk.Button(root, text="Paper", command=lambda: on_button_click("Paper"))
button_scissors = tk.Button(root, text="Scissors", command=lambda: on_button_click("Scissors"))

# Arrange buttons in the window
button_rock.pack(side=tk.LEFT, padx=10, pady=10)
button_paper.pack(side=tk.LEFT, padx=10, pady=10)
button_scissors.pack(side=tk.LEFT, padx=10, pady=10)

# Run the application
root.mainloop()
