from tkinter import *
from timer import timer
from pino import search


def restart():
    root.destroy()
    create_window()


def search_func():
    url = url_entry.get()
    search(url)


def create_window():
    global root
    global url_entry
    global hour
    global minute
    global second

    root = Tk()
    root.geometry("800x600")

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
        text="Set Time Countdown",
        bd="5",
        command=lambda: timer(hour, minute, second, root, search_func),
    )
    timer_button.place(x=70, y=120)

    url_frame = Frame(root)
    url_frame.pack()
    url_label = Label(url_frame, text="Enter URL:")
    url_label.grid(row=0, column=0)
    url_entry = Entry(url_frame)
    url_entry.grid(row=0, column=1)
    search_button = Button(url_frame, text="Search", command=search_func)
    search_button.grid(row=0, column=2)

    reboot_frame = Frame(root)
    reboot_frame.pack()
    restart_button = Button(reboot_frame, text="ReBoot", width=15, command=restart)
    restart_button.grid(row=1, column=1)


create_window()
root.mainloop()
