import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        self.expression = ""

        # Entry widget to display the expression
        self.entry = tk.Entry(root, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons for numbers and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for button in buttons:
            text, row, col = button
            tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col)

    def on_button_click(self, value):
        if value == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif value == 'C':
            self.expression = ""
        else:
            self.expression += value

        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
