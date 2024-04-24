import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the display entry
        self.display = ttk.Entry(master, width=25, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        

        # Create the buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 1
        col = 0
        for button in buttons:
            if button == "=":
                ttk.Button(master, text=button, width=5, command=self.evaluate).grid(row=row, column=col, padx=5, pady=5)
            elif button == "C":
                ttk.Button(master, text=button, width=5, command=self.clear).grid(row=row, column=col, padx=5, pady=5)
            else:
                ttk.Button(master, text=button, width=5, command=lambda x=button: self.add_to_display(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def add_to_display(self, value):
        self.display.insert(tk.END, value)

    def clear(self):
        self.display.delete(0, tk.END)

    def evaluate(self):
        try:
            result = str(eval(self.display.get()))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except ZeroDivisionError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error: Division by zero")
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()