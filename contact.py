import tkinter as tk
from tkinter import messagebox, simpledialog

# Contact book class to manage contacts
class ContactBook:
    def __init__(self):
        self.contacts = {}
        
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False
        
    def get_contact(self, name):
        return self.contacts.get(name, None)
        
    def get_all_contacts(self):
        return self.contacts.items()

# Function to handle adding a contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter contact name:")
    if name:
        phone = simpledialog.askstring("Input", "Enter contact phone number:")
        if phone:
            contact_book.add_contact(name, phone)
            update_contact_list()
            messagebox.showinfo("Success", f"Contact '{name}' added.")
        else:
            messagebox.showwarning("Input Error", "Phone number cannot be empty.")
    else:
        messagebox.showwarning("Input Error", "Name cannot be empty.")

# Function to handle deleting a contact
def delete_contact():
    name = simpledialog.askstring("Input", "Enter contact name to delete:")
    if name:
        if contact_book.delete_contact(name):
            update_contact_list()
            messagebox.showinfo("Success", f"Contact '{name}' deleted.")
        else:
            messagebox.showwarning("Not Found", f"No contact found with name '{name}'.")
    else:
        messagebox.showwarning("Input Error", "Name cannot be empty.")

# Function to display all contacts
def view_contacts():
    contacts = contact_book.get_all_contacts()
    if contacts:
        contacts_str = "\n".join([f"{name}: {phone}" for name, phone in contacts])
        messagebox.showinfo("Contacts", contacts_str)
    else:
        messagebox.showinfo("Contacts", "No contacts available.")

# Function to update the contact list display
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, phone in contact_book.get_all_contacts():
        contact_list.insert(tk.END, f"{name}: {phone}")

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create a ContactBook instance
contact_book = ContactBook()

# Create and arrange buttons
btn_add = tk.Button(root, text="Add Contact", command=add_contact)
btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
btn_delete.pack(pady=5)

btn_view = tk.Button(root, text="View Contacts", command=view_contacts)
btn_view.pack(pady=5)

# Create and arrange contact list
contact_list = tk.Listbox(root, width=50, height=10)
contact_list.pack(pady=10)

# Run the application
root.mainloop()
