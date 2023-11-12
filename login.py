import tkinter as tk
from tkinter import messagebox

def check_credentials():
    # In a real application, you would check the credentials against a database.
    # For this example, let's use hardcoded values.
    valid_username = "user123"
    valid_password = "password123"

    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == valid_username and entered_password == valid_password:
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create and place widgets
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

username_entry.grid(row=0, column=1, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=check_credentials)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
