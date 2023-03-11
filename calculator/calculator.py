import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("계산기")

        # 계산 결과를 표시할 엔트리 위젯
        self.result_entry = tk.Entry(self.master, width=20, font=("Arial", 16))
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # 버튼 생성
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

        # 버튼을 화면에 배치
        row = 1
        col = 0
        for input_text in buttons:
            button = tk.Button(
                self.master,
                text=input_text,
                width=5,
                height=2,
                command=lambda text=input_text: self.button_click(text),
            )
            button.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_button = tk.Button(
            self.master, text="C", width=5, height=2, command=self.clear
        )
        clear_button.grid(row=5, column=0)

    def button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.result_entry.get()))
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(tk.END, result)
            except:
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(tk.END, "write the value")
        else:
            self.result_entry.insert(tk.END, text)

    def clear(self):
        self.result_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
