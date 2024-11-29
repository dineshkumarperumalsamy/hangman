import random
import tkinter as tk
from tkinter import messagebox
# Game setup
guess_words_lists = ["apple", "orange", "yellow", "car"]
gw = random.choice(guess_words_lists)
temp = ["-"] * len(gw)

# Function to check the guessed letter
def checkword():
    iw = input_box.get().strip().lower()
    input_box.delete(0, tk.END)

    if len(iw) != 1:
        messagebox.showerror("Error", "Please enter only one character!")
        return

    if iw in gw:
        for idx, char in enumerate(gw):
            if char == iw:
                temp[idx] = iw
    else:
        messagebox.showinfo("Incorrect Guess", f"'{iw}' is not in the word!")

    update_word_display()

    if "-" not in temp:
        messagebox.showinfo("Congratulations!", f"You've guessed the word: {gw}")
        root.destroy()

# Function to update the word display
def update_word_display():
    word_display.config(text=" ".join(temp))

# Tkinter App Setup
root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("400x500")

# Word display
word_display = tk.Label(root, text=" ".join(temp), font=("Helvetica", 24))
word_display.pack(pady=30)

# Input box
input_box = tk.Entry(root, font=("Helvetica", 18), width=20)
input_box.pack(pady=10)

# Guess button
guess_button = tk.Button(root, text="Guess", font=("Helvetica", 16), command=checkword)
guess_button.pack(pady=10)
root.mainloop()
