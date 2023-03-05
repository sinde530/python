from tkinter import *
from timer import timer
from pino import search, login, github_login
import os


def current_path():
    return os.getcwd()


def restart():
    root.destroy()
    create_window()


def search_func():
    print("1")
    url = url_entry.get()
    print("2")
    # http://gw.meritium.co.kr
    # https://github.com/sinde530/leave_data
    search(url)


def login_information():
    username = login_id_input.get()
    userpassword = login_pw_input.get()
    login(username, userpassword)

    github_url = github_url_entry.get()
    github_id = github_id_input.get()
    github_pw = github_pw_input.get()
    github_login(github_url, github_id, github_pw)


def create_window():
    global root
    global url_entry
    global hour
    global minute
    global second
    global login_id_input
    global login_pw_input
    global github_url_entry
    global github_id_input
    global github_pw_input
    global url_value_save

    root = Tk()
    root.geometry("800x600")
    root.title("Example Test GUI")
    root.iconbitmap(os.path.join(current_path(), "images/unicorn.ico"))

    hour = StringVar()
    minute = StringVar()
    second = StringVar()
    url_value_save = StringVar()

    hour.set("00")
    minute.set("00")
    second.set("00")

    hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
    hourEntry.place(x=80, y=20)
    minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
    minuteEntry.place(x=130, y=20)
    secondEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
    secondEntry.place(x=180, y=20)

    timer_button = Button(
        root,
        text="Start",
        bd="5",
        width=10,
        command=lambda: timer(
            hour, minute, second, root, search_func, login_information
        ),
    )
    timer_button.place(x=70, y=120)

    reboot_frame = Frame(root)
    reboot_frame.pack()
    restart_button = Button(reboot_frame, text="ReBoot", width=15, command=restart)
    restart_button.grid(row=0, column=0, pady=16)

    url_frame = Frame(root)
    url_frame.pack()
    url_label = Label(url_frame, text="Enter URL:")
    url_label.grid(row=1, column=0)
    url_entry = Entry(url_frame, textvariable=url_value_save)
    url_entry.grid(row=1, column=1)

    login_frame = Frame(root)
    login_frame.pack()
    login_id_label = Label(login_frame, text="Email or ID")
    login_id_label.grid(row=2, column=0)
    login_id_input = Entry(login_frame)
    login_id_input.grid(row=2, column=1)
    login_pw_labe = Label(login_frame, text="Password")
    login_pw_labe.grid(row=3, column=0)
    login_pw_input = Entry(login_frame)
    login_pw_input.grid(row=3, column=1)

    github_frame = Frame(root, pady=30)
    github_frame.pack()

    github_url = Label(github_frame, text="github URL:")
    github_url.grid(row=5, column=0)
    github_url_entry = Entry(github_frame)
    github_url_entry.grid(row=5, column=1)

    github_id_label = Label(github_frame, text="github ID")
    github_id_label.grid(row=6, column=0)
    github_id_input = Entry(github_frame)
    github_id_input.grid(row=6, column=1)

    github_pw_label = Label(github_frame, text="github PW")
    github_pw_label.grid(row=7, column=0)
    github_pw_input = Entry(github_frame)
    github_pw_input.grid(row=7, column=1)


create_window()
root.mainloop()
