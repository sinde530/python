import tkinter as tk
from tkinter import filedialog
import pyautogui
import time


def leave_work():
    filename = filedialog.askopenfilename(
        title="select the Leave_Work image file",
        filetypes=(("png files", "*.png"), ("all files", "*.*")),
    )
    try:
        leave_work_button = pyautogui.locateCenterOnScreen(filename)
        pyautogui.click(leave_work_button)
        time.sleep(1)
        pyautogui.keyDown("esc")
        time.sleep(0.4)
    except:
        print("{} 파일을 찾을 수 없습니다.".format(filename))
        return

    pyautogui.hotkey("winleft", "d")
    time.sleep(2)
    pyautogui.hotkey("alt", "tab", "tab", interval=0.1)
    time.sleep(1)
    pyautogui.hotkey("winleft", "x")
    pyautogui.keyDown("u")
    pyautogui.keyDown("s")


root = tk.Tk()
root.title("Leave Work")
root.geometry("600x600")

leave_work_button = tk.Button(root, text="Leave Work", command=leave_work)
leave_work_button.pack()

root.mainloop()
