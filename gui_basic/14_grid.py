from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

btn1 = Button(root, text="button1")
btn2 = Button(root, text="button2")

# btn1.pack(side="left")
# btn2.pack(side="left")

btn1.grid(row=0,column=0)
btn2.grid(row=1,column=1)

root.mainloop() #계속 돌아가 ~ ! 