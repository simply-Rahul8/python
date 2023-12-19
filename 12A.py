import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Expression Calculator")
        
        # create display
        self.display = tk.Entry(master, width=30, font=("Arial", 12))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # create buttons
        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "/", "C"
        ]
        
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.handle_input(x)
            tk.Button(master, text=button, width=5, height=2, command=command).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # create equals button
        tk.Button(master, text="=", width=10, height=2, command=self.calculate).grid(row=5, column=2, columnspan=2, padx=2, pady=2)
    
    def handle_input(self, char):
        if char == "C":
            self.display.delete(0, "end")
        else:
            self.display.insert("end", char)
    
    def calculate(self):
        expression = self.display.get()
        try:
            result = str(eval(expression))
        except:
            result = "Error"
        self.display.delete(0, "end")
        self.display.insert("end", result)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
