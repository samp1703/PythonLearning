import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.display = tk.Entry(master, textvariable=self.display_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        button_layout = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]
        for (text, row, col) in button_layout:
            tk.Button(master, text=text, padx=20, pady=20, font=("Arial", 18),
                      command=lambda t=text: self._on_click(t)).grid(row=row, column=col)
        # Clear and backspace
        tk.Button(master, text="C", padx=20, pady=20, font=("Arial", 18), command=self._clear).grid(row=5, column=0, columnspan=2, sticky="we")
        tk.Button(master, text="←", padx=20, pady=20, font=("Arial", 18), command=self._backspace).grid(row=5, column=2, columnspan=2, sticky="we")

    def _on_click(self, char):
        current = self.display_var.get()
        if char == "=":
            try:
                result = eval(current)
                self.display_var.set(result)
            except Exception:
                self.display_var.set("Error")
        elif current == "0" and char not in (".", "+", "-", "*", "/"):
            self.display_var.set(char)
        else:
            self.display_var.set(current + char)

    def _clear(self):
        self.display_var.set("0")

    def _backspace(self):
        current = self.display_var.get()
        if len(current) > 1:
            self.display_var.set(current[:-1])
        else:
            self.display_var.set("0")

root = tk.Tk()
Calculator(root)
root.mainloop()