import tkinter as tk
from tkinter import messagebox

def rate_password(password):
    score = 0

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    special_characters = "!@#$%^&*()-_=+[]{};:,.<>/?`~"
    if any(c in special_characters for c in password):
        score += 1

    return score

def evaluate_password_security():
    password = entry.get()
    security_score = rate_password(password)

    result_label.config(text="Password Evaluation: ")
    
    if security_score <= 1:
        message = "Your password is insecure. Choose a more complex one."
    elif security_score == 2:
        message = "Your password has a weak security level. Consider choosing a more complex one."
    elif security_score == 3:
        message = "Your password has a moderate security level."
    elif security_score == 4:
        message = "Your password has a good security level."
    else:
        message = "Your password is very secure."

    result_label.config(text=result_label.cget("text") + "\n" + message)

# Creating the Tkinter application
app = tk.Tk()
app.title("Password Security Evaluation")
app.geometry("400x200")

# Interface elements
label = tk.Label(app, text="Enter Your Password:")
label.pack(pady=10)

entry = tk.Entry(app, show="*")
entry.pack(pady=10)

evaluate_button = tk.Button(app, text="Evaluate Password", command=evaluate_password_security)
evaluate_button.pack(pady=10)

result_label = tk.Label(app, text="", wraplength=350, justify="left")
result_label.pack()

# Running the application
app.mainloop()
