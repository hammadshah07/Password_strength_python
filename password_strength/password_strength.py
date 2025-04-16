import tkinter as tk
import re

def check_password_strength():
    password = entry.get()
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Include uppercase letters.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Include lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Include special characters.")

    strength_levels = ["Weak", "Moderate", "Strong", "Very Strong"]
    strength = strength_levels[min(score, len(strength_levels) - 1)]

    result_label.config(text=f"Password Strength: {strength}")

    suggestions_text = "\n".join(suggestions)
    suggestions_label.config(text=f"Suggestions:\n{suggestions_text}")


root = tk.Tk()
root.title("Password Strength Checker")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Enter Password:")
label.grid(row=0, column=0)

entry = tk.Entry(frame, show="*", width=30)
entry.grid(row=0, column=1)

check_button = tk.Button(frame, text="Check Strength", command=check_password_strength)
check_button.grid(row=1, columnspan=2, pady=10)

result_label = tk.Label(frame, text="", fg="blue")
result_label.grid(row=2, columnspan=2)

suggestions_label = tk.Label(frame, text="", fg="red")
suggestions_label.grid(row=3, columnspan=2)

root.mainloop()
