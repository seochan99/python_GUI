from tkinter import *

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

txt = Text(root,width=30,height=5)
txt.pack()

txt.insert(END,"글자를 입력하세요")

e = Entry(root,width=30)
e.pack()
e.insert(0,"한 줄만 입력해용")

def btncmd():
    print(e.get())
    print(txt.get("1.0",END))

    #내용삭제 
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root,text="click", command=btncmd)
btn.pack()
root.mainloop() #계속 돌아가 ~ ! 