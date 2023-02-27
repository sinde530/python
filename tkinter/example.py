import os
import time
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("600x600")
        self.master.title("Example Test GUI")
        self.master.iconbitmap(os.path.join(self.current_path(), 'images/unicorn.ico'))
        self.time = tk.StringVar(self.master)  # self.time 속성 생성
        self.date = tk.StringVar()
        self.date.set("2022-01-01")
        self.create_widgets()
        self.setUrl = tk.StringVar()
        self.setUserId = tk.StringVar()
        self.setUserPassword = tk.StringVar()

    def current_path(self):
        return os.getcwd()

    def console_log(self):
        print(self.current_path())
        print("###### ")

    def create_widgets(self):
        self.console_log()

        # label text for title
        tk.Label(self.master, text="GFG Combobox Widget", background='green',
                 foreground="white", font=("Times New Roman", 15)).grid(row=0, column=1)

        # label
        tk.Label(self.master, text="Select the Month :", font=("Times New Roman", 10)).grid(column=0, row=5, padx=10, pady=25)

        # Combobox creation
        date_time_frame = tk.Frame(root)

        wait_label = tk.Label(date_time_frame, text="대기시간: ")
        wait_label.grid(row=0, column=0)
        self.time.set("10")
        wait_option = tk.OptionMenu(date_time_frame, self.time, "10", "20", "30", "40", "50", "60")
        wait_option.grid(row=0, column=1)

        date_label = tk.Label(date_time_frame, text="날짜: ")
        date_label.grid(row=1, column=0)
        date_entry = tk.Entry(date_time_frame, textvariable=self.date)
        date_entry.grid(row=1, column=1)

        date_time_frame.grid(row=1, column=0)

        # date_time_frame.pack()
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

        homepage_box_frame.grid(row=1, column=0)

        # submit button
        tk.Button(self.master, text="Click", command=self.submit).pack()

    def submit(self):
        print("Selected month:", self.monthchoosen.get())
        print("Wait time:", self.time.get(), "minutes")
        print("URL:", self.set_url.get())
        print("User ID:", self.set_user_id.get())
        print("Password:", self.set_user_password.get())

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
