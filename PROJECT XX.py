import tkinter as tk
from tkinter import messagebox
def check_dick_size():
    x = int(entry.get())
    if x<15:
        messagebox.showinfo("Result","Holy shit how do you even see it? Like dude you need a microscope to even see it! _|_".upper())
    elif x==15:
        messagebox.showinfo("Result","It ain't much but it gets the job done")
    elif x==69:
        messagebox.showinfo("Result","A7a neek!!!!!!!!")
    elif x>69:
        messagebox.showinfo("Result","You got a rocket instead of a dick?".upper())
    else:
        messagebox.showinfo("Result","That's ma nigga :3")
window=tk.Tk()
window.title("Dick Size Checker")
window.geometry("400x250")
label=tk.Label(window,text="Enter your dick size:",font=("Arial",14))
label.pack()
entry=tk.Entry(window,font=("Arial",14))
entry.pack()
button=tk.Button(window,text="Check",command=check_dick_size,font=("Arial",14))
button.pack()
made_by_label=tk.Label(window,text="Made by Yandere Co.",font=("Arial",12))
made_by_label.pack()
window.mainloop()