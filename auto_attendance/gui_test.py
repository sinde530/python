import tkinter as tk
import pyautogui
import time


def leave_work():
    try:
        leave_work_button = pyautogui.locateCenterOnScreen("Leave_Work.png")
        pyautogui.click(leave_work_button)
        time.sleep(1)
        pyautogui.keyDown("esc")
        time.sleep(0.4)
    except:
        print("Leave_Work.png 파일을 찾을 수 없습니다.")
        print("2번째의 이미지 파일을 소싱합니다.")
        # second image
        leave_work_button1 = pyautogui.locateCenterOnScreen("Leave_Work1.png")
        pyautogui.click(leave_work_button1)
        time.sleep(1)
        pyautogui.keyDown("esc")
        time.sleep(0.4)

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
