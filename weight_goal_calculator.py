import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        goal = goal_var.get()
        weight_change = float(weight_change_entry.get())
        weeks = float(weeks_entry.get())
        current_weight = float(weight_entry.get())

        daily_calorie_change = (weight_change * 3500) / (weeks * 7)
        min_protein, max_protein = current_weight * 0.8, current_weight * 1.2

        result = f"To {goal} {weight_change} lbs in {weeks} weeks:\n"
        result += f"Adjust your daily intake by approximately {daily_calorie_change:.2f} calories.\n"
        result += f"Recommended daily protein intake: {min_protein:.2f}g - {max_protein:.2f}g."

        messagebox.showinfo("Results", result)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Weight Goal Calculator")

# Goal selection
goal_var = tk.StringVar(value="lose")
tk.Label(root, text="Select Goal:").pack()
tk.Radiobutton(root, text="Lose Weight", variable=goal_var, value="lose").pack()
tk.Radiobutton(root, text="Gain Weight", variable=goal_var, value="gain").pack()

# Create entry fields for weight, weight change goal, and time frame
weight_entry = tk.Entry(root)
weight_change_entry = tk.Entry(root)
weeks_entry = tk.Entry(root)

# Input fields
tk.Label(root, text="Enter current weight (lbs):").pack()
weight_entry.pack()

tk.Label(root, text="Enter weight change goal (lbs):").pack()
weight_change_entry.pack()

tk.Label(root, text="Enter time frame (weeks):").pack()
weeks_entry.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack()

# Run GUI
root.mainloop()
