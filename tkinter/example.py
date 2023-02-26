# -*- coding: utf-8 -*-

from tkinter import *
import os


def current_path():
    return os.getcwd()


def console_log():
    print(current_path())
    print("###### ")


def main():
    root = Tk()
    root.geometry("600x600")
    console_log()

    root.title("Example Test GUI")
    image_path = os.path.join(current_path(), "images/unicorn.ico")

    root.iconbitmap(image_path)

    label = Label(root, text="Hello World1")
    label.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
