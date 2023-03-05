from tkinter import *
from pino import search
import json
import os

save_file = "config.json"


def save_file_value():
    with open(save_file, "w") as f:
        json.dump(save_value.get(), f)


def search_func():
    url = url_entry.get()
    search(url)


def create_window():
    global root
    global url_entry
    global save_value

    root = Tk()
    root.geometry("800x600")
    root.title("Example Test GUI")

    if os.path.isfile(save_file):
        with open(save_file, "r") as f:
            save_value = StringVar(value=json.load(f))
    else:
        save_value = StringVar(value="")

    url_frame = Frame(root)
    url_frame.pack()
    url_label = Label(url_frame, text="Enter URL:")
    url_label.grid(row=1, column=0)
    url_entry = Entry(url_frame, textvariable=save_value)
    url_entry.grid(row=1, column=1)

    button = Button(root, bd="10", text="Start", command=search_func)
    button.pack()

    root.protocol("WM_DELETE_WINDOW", save_file_value)
    root.mainloop()


create_window()
