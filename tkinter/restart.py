from tkinter import *

root = Tk()


def restart():
    global root
    global lbl
    global txt
    global btn

    try:
        root.state()
        root.destroy()
    finally:
        root = Tk()
        lbl = Label(root, text="Reboot")
        lbl.grid(row=0, column=0)
        txt = Entry(root)
        txt.grid(row=0, column=1)
        btn = Button(root, text="OK", width=15, command=restart)
        btn.grid(row=1, column=1)

        root.geometry("200x100+400+300")
        root.mainloop()


lbl = Label(root, text="Reboot")
lbl.grid(row=0, column=0)
txt = Entry(root)
txt.grid(row=0, column=1)
btn = Button(root, text="OK", width=15, command=restart)
btn.grid(row=1, column=1)
root.geometry("200x100+400+500")

root.mainloop()
