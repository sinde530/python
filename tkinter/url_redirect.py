import time
import tkinter as tk
from selenium import webdriver


def search():
    url = url_entry.get()
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()
    time.sleep(2400)


root = tk.Tk()

url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

root.mainloop()
