import string
from random import shuffle
import tkinter as tk
from tkinter import messagebox

# Function to generate a single password
def create_password(lowercase_count, uppercase_count, special_count, number_count):
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    special_characters = list("!@#$%^&*()_+-=[]{}|;:',.<>?/~`")
    number_characters = list("0123456789")

    shuffle(lowercase_letters)
    shuffle(uppercase_letters)
    shuffle(special_characters)
    shuffle(number_characters)

    password_chars = (
        lowercase_letters[:lowercase_count] +
        uppercase_letters[:uppercase_count] +
        special_characters[:special_count] +
        number_characters[:number_count]
    )

    shuffle(password_chars)
    return ''.join(password_chars)

# Function to handle button click
def generate_passwords():
    try:
        total = int(num_passwords.get())
        lc = int(lowercase_count.get())
        uc = int(uppercase_count.get())
        sc = int(special_count.get())
        nc = int(number_count.get())

        output_box.delete("1.0", tk.END)  # Clear output box

        for i in range(total):
            pwd = create_password(lc, uc, sc, nc)
            output_box.insert(tk.END, f"{i+1}. {pwd}\n")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for all fields.")

# Function to copy output to clipboard
def copy_to_clipboard():
    generated = output_box.get("1.0", tk.END).strip()
    if generated:
        root.clipboard_clear()
        root.clipboard_append(generated)
        messagebox.showinfo("Copied", "Passwords copied to clipboard!")
    else:
        messagebox.showwarning("No Passwords", "Nothing to copy yet.")




# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x500")
root.resizable(False, False)

# Title
tk.Label(root, text="🔐 Password Generator", font=("Arial", 18, "bold")).pack(pady=10)

# Input frame
frame = tk.Frame(root)
frame.pack(pady=5)

# Input fields
tk.Label(frame, text="Number of passwords:").grid(row=0, column=0, sticky='e')
tk.Label(frame, text="Lowercase letters:").grid(row=1, column=0, sticky='e')
tk.Label(frame, text="Uppercase letters:").grid(row=2, column=0, sticky='e')
tk.Label(frame, text="Special characters:").grid(row=3, column=0, sticky='e')
tk.Label(frame, text="Numbers:").grid(row=4, column=0, sticky='e')

num_passwords = tk.Entry(frame)
lowercase_count = tk.Entry(frame)
uppercase_count = tk.Entry(frame)
special_count = tk.Entry(frame)
number_count = tk.Entry(frame)

num_passwords.grid(row=0, column=1)
lowercase_count.grid(row=1, column=1)
uppercase_count.grid(row=2, column=1)
special_count.grid(row=3, column=1)
number_count.grid(row=4, column=1)

# Generate button
tk.Button(root, text="Generate Passwords", command=generate_passwords, bg="#4CAF50", fg="white", width=25).pack(pady=10)

# Output box
output_box = tk.Text(root, height=10, width=50)
output_box.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white").pack(pady=5)

# Start the GUI loop
root.mainloop()
