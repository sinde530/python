import pyautogui
import time


def leave_work(file_name):
    try:
        leave_work_button = pyautogui.locateCenterOnScreen(file_name)
        print("1", leave_work_button)
    except FileNotFoundError:
        print(f"{file_name} 파일을 찾을 수 없습니다.")
        print("2번째의 이미지 파일을 소싱합니다.")

        # second image
        leave_work_button1 = pyautogui.locateCenterOnScreen("image2.png")
        print("2", leave_work_button1)


# setTimeOut
time.sleep(60)

leave_work("image1.png")
