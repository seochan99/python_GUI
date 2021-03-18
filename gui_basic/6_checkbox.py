from tkinter import *

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

checkvar = IntVar() #chkvar 에 int 형으로 gap을 wjwkd 한다. 
checkbox = Checkbutton(root,text="오늘 그만보자", variable=checkvar)
# checkbox.select() #자동선택 처리
# checkbox.deselect() #선택 해제 처리 
checkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root,text="일주일동ㅇ안 보지 ㅇ낳기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(checkvar.get())
    print(chkvar2.get())

btn = Button(root,text="click", command=btncmd)
btn.pack()

root.mainloop() #계속 돌아가 ~ ! 