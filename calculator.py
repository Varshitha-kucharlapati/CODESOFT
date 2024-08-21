import tkinter as tk

# Function to update the expression in the entry widget
def update_expression(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

# Function to evaluate the expression and display the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for displaying the expression
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)  # Clear button spans 4 columns
]

# Create and place buttons on the grid
for (text, row, column, *span) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, command=clear_entry)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: update_expression(t))
    
    if span:
        btn.grid(row=row, column=column, columnspan=span[0])
    else:
        btn.grid(row=row, column=column)

# Start the main event loop
root.mainloop()
