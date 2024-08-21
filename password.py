import tkinter as tk
import random
import string

def generate_password():
    # Get the values from the input fields and checkboxes
    length = int(entry_length.get())
    include_digits = var_digits.get()
    include_special = var_special_chars.get()
    
    # Validate the length input
    if length < 1:
        result_label.config(text="Password length must be at least 1.")
        return
    
    # Build the character set based on user input
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Display the generated password
    result_label.config(text=f"Generated Password: {password}")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_length = tk.Entry(root, width=10)
entry_length.grid(row=0, column=1, padx=10, pady=5)

var_digits = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Digits", variable=var_digits).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

var_special_chars = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Special Characters", variable=var_special_chars).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Generated Password will appear here.")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
