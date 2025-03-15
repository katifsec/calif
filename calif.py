import tkinter as tk

# Function to update the entry field
def press(num):
    entry_var.set(entry_var.get() + str(num))

# Function to perform calculations
def calculate():
    try:
        math_exp = entry_var.get()

        # Handling percentage (X% of Y)
        if '%' in math_exp and len(math_exp.split('%')) == 2:
            num1, num2 = map(float, math_exp.split('%'))
            entry_var.set((num1 * num2) / 100)

        # Handling division by zero
        elif '/' in math_exp:
            num1, num2 = map(float, math_exp.split('/'))
            if num2 == 0:
                entry_var.set("Cannot divide by zero")
            else:
                entry_var.set(num1 / num2)
        
        # Normal calculations
        else:
            result = eval(math_exp)
            entry_var.set(result)

    except:
        entry_var.set("Error")

# Function to clear entry field
def clear():
    entry_var.set("")

# GUI Window Setup
root = tk.Tk()
root.title("Advanced Calculator")

# ✅ FIXED SIZE – FULL FIT WITHOUT CUTTING
root.geometry("400x550")  
root.resizable(False, False)  

root.configure(bg="black")

# Entry Field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 22), justify="right", bd=10, relief="ridge", bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=15, sticky="news")

# Gradient Button Colors
gradient_colors = {
    "C": "#FF5733", "=": "#28B463", "/": "#3498DB", "*": "#8E44AD",
    "+": "#F39C12", "-": "#E74C3C", "%": "#2ECC71", "mod": "#16A085",
    "Exit": "#17202A"
}

# Buttons Layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('=', 5, 1), ('mod', 5, 2), ('Exit', 5, 3)
]

# Creating Buttons Dynamically
for (text, row, col) in buttons:
    bg_color = gradient_colors.get(text, "#2C3E50")  # Default gradient color

    btn = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: press(t) if t not in ['C', '=', 'mod', 'Exit'] else calculate() if t == '=' else clear() if t == 'C' else root.quit() if t == 'Exit' else press('%'),
                    height=2, width=8, bg=bg_color, fg="white", activebackground="#D5DBDB", relief="ridge")

    btn.grid(row=row, column=col, padx=5, pady=5, sticky="news")

# Adjusting Row & Column Sizes
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Running GUI
root.mainloop()
