import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.equation = ""
        
        # Entry widget to display input/output
        self.display = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 1, 4), ('^', 2, 4), ('√', 3, 4), ('(', 4, 4),
            (')', 4, 5), ('sin', 1, 5), ('cos', 2, 5), ('tan', 3, 5),
            ('log', 1, 6), ('exp', 2, 6), ('fact', 3, 6)
        ]
        
        for (text, row, column) in buttons:
            tk.Button(root, text=text, width=8, height=2, font=("Arial", 14), 
                      command=lambda t=text: self.button_click(t)).grid(row=row, column=column, padx=5, pady=5)
    
    def button_click(self, value):
        if value == '=':
            try:
                self.equation = self.equation.replace('^', '**')
                result = eval(self.equation)
                self.equation = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.equation)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input\n{e}")
        
        elif value == 'C':
            self.equation = ""
            self.display.delete(0, tk.END)
        
        elif value == '√':
            try:
                result = math.sqrt(float(self.equation))
                self.equation = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.equation)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input\n{e}")
        
        elif value == 'log':
            try:
                result = math.log10(float(self.equation))
                self.equation = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.equation)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input\n{e}")
        
        elif value == 'exp':
            try:
                result = math.exp(float(self.equation))
                self.equation = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.equation)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input\n{e}")
        
        elif value == 'fact':
            try:
                result = math.factorial(int(self.equation))
                self.equation = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.equation)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input\n{e}")
        
        elif value in ['sin', 'cos', 'tan']:
            try:
                func = getattr(math, value)
                result = func(math.radians(float(self.equation)))
                self.equation = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.equation)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input\n{e}")
        
        else:
            self.equation += value
            self.display.insert(tk.END, value)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
