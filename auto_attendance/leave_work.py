import pyautogui
import time


def leave_work(file_name):
    try:
        leave_work_button = pyautogui.locateCenterOnScreen(file_name)
        pyautogui.click(leave_work_button)
        print("1", leave_work_button)
        time.sleep(1)

        pyautogui.keyDown("esc")
        time.sleep(0.4)
    except FileNotFoundError:
        print(f"{file_name} 파일을 찾을 수 없습니다.")
        print("2번째의 이미지 파일을 소싱합니다.")

        # second image
        leave_work_button1 = pyautogui.locateCenterOnScreen("image2.png")
        print("2", leave_work_button1)

        if leave_work_button1:
            pyautogui.click(leave_work_button1)
            time.sleep(1)
            pyautogui.keyDown("esc")
            time.sleep(0.4)
        else:
            print("이미지를 찾지 못하였거나, 알 수 없는 오류가 발생하였습니다.")
            print("종료합니다.")
            return


pyautogui.hotkey("winleft", "d")
time.sleep(2)
pyautogui.hotkey("alt", "tab", "tab", interval=0.1)

# setTimeOut
time.sleep(1200)

leave_work("image1.png")
pyautogui.hotkey("winleft", "x")
pyautogui.keyDown("u")
pyautogui.keyDown("s")
