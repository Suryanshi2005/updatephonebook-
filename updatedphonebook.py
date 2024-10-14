import tkinter as tk
from tkinter import messagebox

# Phone book dictionary to store contact information
phone_book = {}

# Functions to manage phone book operations
def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    if name and number:
        phone_book[name] = number
        messagebox.showinfo("Success", f"Added {name} with number {number}.")
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both name and number.")

def search_contact():
    name = name_entry.get()
    if name in phone_book:
        messagebox.showinfo("Contact Found", f"{name}: {phone_book[name]}")
    else:
        messagebox.showwarning("Not Found", f"{name} not found in the phone book.")
    name_entry.delete(0, tk.END)

def delete_contact():
    name = name_entry.get()
    if name in phone_book:
        del phone_book[name]
        messagebox.showinfo("Success", f"Deleted {name} from the phone book.")
    else:
        messagebox.showwarning("Not Found", f"{name} not found in the phone book.")
    name_entry.delete(0, tk.END)

def display_contacts():
    if phone_book:
        contacts = "\n".join([f"{name}: {number}" for name, number in phone_book.items()])
        messagebox.showinfo("Phone Book", contacts)
    else:
        messagebox.showinfo("Phone Book", "Phone book is empty.")

# GUI setup
root = tk.Tk()
root.title("Phone Book")

# Labels and Entry fields
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Number:").grid(row=1, column=0)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1)

# Buttons for actions
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=2, column=0, padx=5, pady=5)

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.grid(row=2, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=3, column=0, padx=5, pady=5)

display_button = tk.Button(root, text="Display Contacts", command=display_contacts)
display_button.grid(row=3, column=1, padx=5, pady=5)

# Run the application
root.mainloop()
