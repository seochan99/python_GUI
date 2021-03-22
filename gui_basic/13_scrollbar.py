from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  


frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1,32):
    listbox.insert(END,str(i)+"일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)


root.mainloop() #계속 돌아가 ~ ! 