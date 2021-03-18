from tkinter import *

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

label1 = Label(root,text="안녕하세용")
label1.pack()

# photo= PhotoImage(file="gui_basic")
# label2 = Label(root,image=photo)
# label2.pack()

def change():
    label1.config(text="또 만낭")

btn= Button(root,text="클릭", command=change)
btn.pack()
root.mainloop() #계속 돌아가 ~ ! 