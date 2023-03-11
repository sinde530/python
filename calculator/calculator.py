import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.result_entry = tk.Entry(self.master, width=20, font=("Arial", 16))
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            "7",
            "8",
            "9",
            "+",
            "4",
            "5",
            "6",
            "-",
            "1",
            "2",
            "3",
            "*",
            "0",
            ".",
            "=",
            "/",
        ]

        row = 1
        col = 0
        for input_text in buttons:
            button = tk.Button(
                self.master,
                text=input_text,
                width=5,
                height=2,
                command=lambda text=input_text: self.handle_button_click(text),
            )
            button.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_button = tk.Button(
            self.master,
            text="C",
            width=5,
            height=2,
            command=self.handle_clear_button_click,
        )
        clear_button.grid(row=5, column=0)

    def handle_button_click(self, text):
        if text == "=":
            self.calculate()
        else:
            self.handle_text_click(text)

    def calculate(self):
        try:
            result = str(eval(self.result_entry.get()))
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(tk.END, result)
        except:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(tk.END, "Error")

    def handle_text_click(self, button_text):
        self.result_entry.insert(tk.END, button_text)

    def handle_clear_button_click(self):
        self.result_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
