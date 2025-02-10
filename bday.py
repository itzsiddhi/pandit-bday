import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

def countdown(target_date, label):
    def update():
        now = datetime.datetime.now()
        time_left = target_date - now
        if time_left.total_seconds() <= 0:
            label.config(text="🎉 It's Aryan's Birthday! 🎉")
        else:
            label.config(text=f"Time left for Aryan's Birthday:\n{time_left}")
            root.after(1000, update)  # Update every 1 second
    update()

# Show birthday message
def show_birthday_message():
    messagebox.showinfo("🎂 Happy Birthday Aryan! 🎂", 
                        "Wishing you a day filled with joy, laughter, and all the things you love!\n"
                        "Stay the amazing, emotional yet funny person you are! 😃🎈\n"
                        "Here’s to new adventures, genuine conversations, and the beginning of many unforgettable memories!")

# Fun fact
def fun_fact():
    messagebox.showinfo("Fun Fact!", "Aryan is super emotional yet funny, a rare and awesome combo! ✨")

# Quiz
def quiz():
    answer = simpledialog.askstring("Quiz Time!", "What is the one song that is relatable to both of us?")
    if answer and answer.lower().strip() == "abhi na jao chod kar":
        messagebox.showinfo("Quiz Result", "Correct! You really know us well! 😎")
    else:
        messagebox.showinfo("Quiz Result", "Oops! The correct answer is 'Abhi Na Jao Chhod Ke' 🎶")

# Cake meme
def show_cake_meme():
    messagebox.showinfo("🎂 Cake Time! 🎂", """ 
        ,   ,   ,   ,   
        |\\_/|  |\\_/|  
        | @ @   @ @ |  
        |   <>   <>  |  
        |  _()()_  |  
         \\_______/  
        Happy Birthday pandit! 🎂
    """)

# Main window
root = tk.Tk()
root.title("Aryan's Birthday Countdown")
root.geometry("400x300")

label = tk.Label(root, text="", font=("Arial", 14), fg="white")
label.pack(pady=20)

# Set target birthday date
target_date = datetime.datetime(2025, 2, 12, 0, 0, 0)
countdown(target_date, label)

# Buttons
tk.Button(root, text="Show Birthday Message", command=show_birthday_message).pack(pady=5)
tk.Button(root, text="Fun Fact", command=fun_fact).pack(pady=5)
tk.Button(root, text="Take Quiz", command=quiz).pack(pady=5)
tk.Button(root, text="Show Cake Meme", command=show_cake_meme).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

root.mainloop()
