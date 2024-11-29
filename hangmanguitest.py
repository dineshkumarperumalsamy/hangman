import random
import tkinter as tk
from tkinter import messagebox

# Game setup
guess_words_lists = ["apple", "orange", "yellow", "car"]
gw = random.choice(guess_words_lists)
temp = ["-"] * len(gw)
incorrect_guesses = []
max_attempts = 6

# Function to check the guessed letter
def checkword():
    global max_attempts
    iw = input_box.get().strip().lower()
    input_box.delete(0, tk.END)

    if len(iw) != 1 or not iw.isalpha():
        messagebox.showerror("Error", "Please enter only one alphabet!")
        return

    if iw in gw:
        for idx, char in enumerate(gw):
            if char == iw:
                temp[idx] = iw
    elif iw not in incorrect_guesses:
        incorrect_guesses.append(iw)
        max_attempts -= 1
        messagebox.showinfo("Incorrect Guess", f"'{iw}' is not in the word!")
    else:
        messagebox.showwarning("Warning", f"You already guessed '{iw}'!")

    update_word_display()

    if "-" not in temp:
        messagebox.showinfo("Congratulations!", f"You've guessed the word: {gw}")
        reset_game()
    elif max_attempts == 0:
        messagebox.showinfo("Game Over", f"You've run out of attempts! The word was: {gw}")
        reset_game()

# Function to update the word display
def update_word_display():
    word_display.config(text=" ".join(temp))
    incorrect_label.config(text=f"Incorrect Guesses: {', '.join(incorrect_guesses)}")
    attempts_label.config(text=f"Attempts Left: {max_attempts}")

# Function to reset the game
def reset_game():
    global gw, temp, incorrect_guesses, max_attempts
    gw = random.choice(guess_words_lists)
    temp = ["-"] * len(gw)
    incorrect_guesses = []
    max_attempts = 6
    update_word_display()

# Tkinter App Setup
root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("400x500")

# Word display
word_display = tk.Label(root, text=" ".join(temp), font=("Helvetica", 24))
word_display.pack(pady=30)

# Incorrect guesses
incorrect_label = tk.Label(root, text="Incorrect Guesses: ", font=("Helvetica", 14), fg="red")
incorrect_label.pack()

# Attempts left
attempts_label = tk.Label(root, text=f"Attempts Left: {max_attempts}", font=("Helvetica", 14), fg="white")
attempts_label.pack()

# Input box
input_box = tk.Entry(root, font=("Helvetica", 18), width=20)
input_box.pack(pady=10)

# Guess button
guess_button = tk.Button(root, text="Guess", font=("Helvetica", 16), command=checkword)
guess_button.pack(pady=10)

# Restart button
restart_button = tk.Button(root, text="Restart Game", font=("Helvetica", 14), command=reset_game)
restart_button.pack(pady=10)

root.mainloop()
