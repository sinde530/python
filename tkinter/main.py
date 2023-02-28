import time
from tkinter import *
from selenium import webdriver


def timer():
    try:
        # stored in here :temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if temp == 0:
            search()
            break

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


def search():
    url = url_entry.get()
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()
    time.sleep(10)


def restart():
    root.destroy()  # 이전 윈도우 창을 닫음
    create_window()  # 새로운 윈도우 창 생성


def create_window():
    global root
    global url_entry
    global hour
    global minute
    global second

    root = Tk()
    root.geometry("800x600")

    # Declaration of variables
    hour = StringVar()
    minute = StringVar()
    second = StringVar()

    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")

    hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
    hourEntry.place(x=80, y=20)

    minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
    minuteEntry.place(x=130, y=20)

    secondEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
    secondEntry.place(x=180, y=20)

    # button widget
    timer_button = Button(root, text="Set Time Countdown", bd="5", command=timer)
    timer_button.place(x=70, y=120)

    # URL 입력 위젯
    url_frame = Frame(root)
    url_frame.pack()
    url_label = Label(url_frame, text="Enter URL:")
    url_label.grid(row=0, column=0)
    url_entry = Entry(url_frame)
    url_entry.grid(row=0, column=1)
    search_button = Button(url_frame, text="Search", command=search)
    search_button.grid(row=0, column=2)

    # Reboot 버튼 위젯
    reboot_frame = Frame(root)
    reboot_frame.pack()
    restart_button = Button(reboot_frame, text="ReBoot", width=15, command=restart)
    restart_button.grid(row=1, column=1)


create_window()
root.mainloop()
