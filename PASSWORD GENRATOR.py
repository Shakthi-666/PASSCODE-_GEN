import tkinter as tk
import string
import random
from tkinter import messagebox

# Password generator function
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number!")
        return

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_chars, k=length))
    password_var.set(password)

def copy_password():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy!")

# --- Tkinter UI Setup ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# Label and Entry for password length
tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify='center')
length_entry.pack()

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white")
generate_btn.pack(pady=10)

# Display Password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, state="readonly", justify='center').pack(pady=5)

# Copy to Clipboard Button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_password, font=("Arial", 12), bg="#2196F3", fg="white")
copy_btn.pack(pady=10)

# Run the App
root.mainloop()
