from tkinter import *


def get_text():
    print(text_entry1.get())
    print(text_entry2.get())


root = Tk()
root.geometry("320x240")
root.title("Test Tkinter")
text_value = StringVar()

frame = Frame(root)
frame.pack()

text_entry1 = Entry(frame, width=30, bg="light blue", textvariable=text_value)
text_entry1.insert(0, "")
text_entry1.pack(pady=15)

text_entry2 = Entry(frame, width=25, bg="light blue")
text_entry2.insert(0, "insert second text")
text_entry2.pack(pady=0)

button = Button(frame, text="Get Text", command=get_text)
button.pack(pady=20)

root.mainloop()
