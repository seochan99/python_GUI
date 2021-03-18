import tkinter.ttk as ttk 
from tkinter import *

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

values= [str(i) +"일" for i in range(1,32)]
combobox = ttk.Combobox(root,height=5,values=values, state="readonly")
combobox.pack()
combobox.set("카드 결제일") #제일 처음뜨는 글 

def btncmd():
    print(combobox.get())

btn = Button(root,text="click", command=btncmd)
btn.pack()

root.mainloop() #계속 돌아가 ~ ! 