from tkinter import *
from timer import timer
from pino import search, login
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
    search(url)
    print("3")


def login_information():
    username = login_id_input.get()
    userpassword = login_pw_input.get()
    login(username, userpassword)


def create_window():
    global root
    global url_entry
    global hour
    global minute
    global second
    global login_id_input
    global login_pw_input

    root = Tk()
    root.geometry("800x600")
    root.title("Example Test GUI")
    root.iconbitmap(os.path.join(current_path(), "images/unicorn.ico"))

    hour = StringVar()
    minute = StringVar()
    second = StringVar()

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

    url_frame = Frame(root, pady=24)
    url_frame.pack()
    url_label = Label(url_frame, text="Enter URL:")
    url_label.grid(row=0, column=0)
    url_entry = Entry(url_frame)
    url_entry.grid(row=0, column=1)

    reboot_frame = Frame(root)
    reboot_frame.pack()
    restart_button = Button(reboot_frame, text="ReBoot", width=15, command=restart)
    restart_button.grid(row=1, column=1)

    login_frame = Frame(root, pady=16)
    login_frame.pack()
    login_id_label = Label(login_frame, text="Email or ID")
    login_id_label.grid(row=1, column=0)
    login_id_input = Entry(login_frame)
    login_id_input.grid(row=1, column=1)
    login_pw_labe = Label(login_frame, text="Password")
    login_pw_labe.grid(row=2, column=0)
    login_pw_input = Entry(login_frame)
    login_pw_input.grid(row=2, column=1)


create_window()
root.mainloop()
