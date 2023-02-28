import time
import tkinter as tk
from selenium import webdriver


def search():
    url = url_entry.get()
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()
    time.sleep(10)


root = tk.Tk()
root.geometry("800x600")

url_label = tk.Label(root, text="Enter URL:")
url_label.grid(row=0, column=0)

url_entry = tk.Entry(root)
url_entry.grid(row=0, column=1)

search_button = tk.Button(root, text="Search", command=search)
search_button.grid(row=0, column=2)

root.mainloop()
