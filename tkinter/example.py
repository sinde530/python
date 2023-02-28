import os
import tkinter as tk


class Application(tk.Frame):
    """
    Args:
        tk (_type_): _description_
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x600")
        self.master.title("Example Test GUI")
        self.master.iconbitmap(os.path.join(self.current_path(), "images/unicorn.ico"))
        self.time = tk.StringVar(self.master)  # self.time 속성 생성
        self.date = tk.StringVar()
        self.date.set("2022-01-01")
        self.setUrl = tk.StringVar()  # move setUrl creation before create_widgets
        self.setUserId = tk.StringVar()
        self.setUserPassword = tk.StringVar()
        self.create_widgets()

    def current_path(self):
        return os.getcwd()

    def console_log(self):
        print(self.current_path())
        print("###### ")

    def create_widgets(self):
        self.console_log()

        # label text for title
        tk.Label(
            self.master,
            text="GFG Combobox Widget",
            bg="green",
            fg="white",
            font=("Times New Roman", 15),
        ).grid(row=0, column=0, padx=10, pady=25)

        # Combobox creation
        date_time_frame = tk.Frame(root)

        wait_label = tk.Label(date_time_frame, text="대기시간: ")
        wait_label.grid(row=1, column=0)
        self.time.set("10")
        wait_option = tk.OptionMenu(
            date_time_frame, self.time, "10", "20", "30", "40", "50", "60"
        )
        wait_option.grid(row=1, column=1)

        date_label = tk.Label(date_time_frame, text="날짜: ")
        date_label.grid(row=2, column=0)
        date_entry = tk.Entry(date_time_frame, textvariable=self.date)
        date_entry.grid(row=2, column=1)

        date_time_frame.grid(row=2, column=0)

        homepage_box_frame = tk.Frame(root)

        url_label = tk.Label(homepage_box_frame, text="input to url text")
        url_label.pack(side=tk.LEFT)
        url_entry = tk.Entry(homepage_box_frame, textvariable=self.setUrl)
        url_entry.pack(side=tk.LEFT)

        id_label = tk.Label(homepage_box_frame, text="input to userId text")
        id_label.pack(side=tk.LEFT)
        id_entry = tk.Entry(homepage_box_frame, textvariable=self.setUserId)
        id_entry.pack(side=tk.LEFT)

        pw_label = tk.Label(homepage_box_frame, text="input to userPassword text")
        pw_label.pack(side=tk.LEFT)
        pw_entry = tk.Entry(homepage_box_frame, textvariable=self.setUserPassword)
        pw_entry.pack(side=tk.LEFT)

        homepage_box_frame.grid(row=4, column=0)

        # submit button
        tk.Button(self.master, text="Click", command=self.submit).grid(row=6, column=0)

    def submit(self):
        # print("Selected month:", self.monthchoosen.get())
        print("Wait time:", self.time.get(), "minutes")
        print("URL:", self.setUrl.get())
        print("User ID:", self.setUserId.get())
        print("Password:", self.setUserPassword.get())


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
