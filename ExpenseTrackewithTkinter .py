import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# Variables to store expenses
expenses = []

# Function to add an expense
def add_expense():
    try:
        amount = float(entry_amount.get())
        category = entry_category.get()

        if category and amount >= 0:
            expenses.append((category, amount))
            messagebox.showinfo("Success", "Expense added successfully!")
            entry_amount.delete(0, tk.END)
            entry_category.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter valid values!")
    except ValueError:
        messagebox.showwarning("Input Error", "Amount must be a number.")

# Function to show total expenses
def show_total():
    total = sum([expense[1] for expense in expenses])
    messagebox.showinfo("Total Expenses", f"Total Expenses: {total}")

# Function to reset all expenses
def reset_expenses():
    global expenses
    expenses = []
    messagebox.showinfo("Reset", "All expenses have been reset!")

# Labels and Entry fields
label_amount = tk.Label(root, text="Amount:")
label_amount.grid(row=0, column=0)

entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

label_category = tk.Label(root, text="Category:")
label_category.grid(row=1, column=0)

entry_category = tk.Entry(root)
entry_category.grid(row=1, column=1)

# Buttons
btn_add = tk.Button(root, text="Add Expense", command=add_expense)
btn_add.grid(row=2, column=0)

btn_show_total = tk.Button(root, text="Show Total", command=show_total)
btn_show_total.grid(row=2, column=1)

btn_reset = tk.Button(root, text="Reset Expenses", command=reset_expenses)
btn_reset.grid(row=3, column=0, columnspan=2)

# Run the main loop
root.mainloop()
