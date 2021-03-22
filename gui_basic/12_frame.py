from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

Label(root,text="메뉴를 선택해 주세용").pack(side="top")

Button(root,text="주문하기").pack(side="bottom")

#햄버거 집 방문 
frame_burger = Frame(root,relief="solid",bd=1)
frame_burger.pack(side = "left",fill="both", expand=True)

Button(frame_burger,text="ham").pack()
Button(frame_burger,text="ch").pack()
Button(frame_burger,text="to").pack()

frame_drink = LabelFrame(root,text="음료")
frame_drink.pack(side="right",fill="both", expand=True)
Button(frame_drink,text="sida").pack()
Button(frame_drink,text="coke").pack()

root.mainloop() #계속 돌아가 ~ ! 