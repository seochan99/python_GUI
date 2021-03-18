import tkinter.ttk as ttk 
from tkinter import *
import time 
root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

progressbar = ttk.Progressbar(root,maximum=100,mode="determinate") 
progressbar.start(10)
progressbar.pack()

p_var=DoubleVar()
progressbar2 = ttk.Progressbar(root,maximum=100,length=50, variable=p_var)
progressbar2.pack() 

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01)

        p_var.set(i)
        progressbar2.update() #update 기술 
        print(p_var.get())

btn2 = Button(root,text="start",command=btncmd2)
btn2.pack()
def btncmd():
    progressbar.stop()

btn = Button(root,text="click", command=btncmd)
btn.pack()

root.mainloop() #계속 돌아가 ~ ! 