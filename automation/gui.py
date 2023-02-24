import tkinter as tk

root = tk.Tk()
root.geometry("320x240") # root 윈도우는 pack()이 필요없다.
root.title("Frame Test")

frame = tk.Frame(root, bd=5,bg='light blue', relief = 'groove') # 메인프레임
frame.pack()

l_frame = tk.Frame(root, bd=40,bg='white') # 왼쪽프레임
l_frame.pack(side=tk.LEFT)

r_frame = tk.Frame(root) # 오른쪽프레임
r_frame.pack(side=tk.RIGHT)

label = tk.Label(frame,text = 'Hello Tkinter!') # top 쪽에 올라감
label.pack()

button1 = tk.Button(l_frame,text='Button 1') # 기본형
button1.pack(padx = 10, pady = 10)

button2 = tk.Button(r_frame,text='Button 2' , bd = 5, bg = 'light blue',)
button2.pack(padx = 10, pady = 10)

button3 = tk.Button(l_frame,text='Button 3', bd = 5, bg = 'light green')
button3.pack(padx = 10, pady = 10)

button4 = tk.Button(r_frame,text='Button 4', relief = 'sunken')
button4.pack(padx = 10, pady = 10)

root.mainloop()
