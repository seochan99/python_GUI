from tkinter import *

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

btn1 = Button(root, text="버튼1") #버튼 생성
btn1.pack() # 버튼 보이게 만들기 

btn2 = Button(root, padx = 5 , pady = 10, text ="버튼2")
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text ="버튼3")
btn3.pack()

btn4  = Button(root,width=10,height=3,text="버튼4")
btn4.pack()

btn5  = Button(root,fg="red",bg="yellow",text="버튼5")
btn5.pack()

# Photo = PhotoImage(file = "sdad")
# btn6= Button(root,image=photo)
# btn6.pack() #내가 그린 그림을 버튼으로 만들기 
def btncmd():
    print("버튼이 클릭되었어용")

btn7 = Button(root,text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop() #계속 돌아가 ~ ! 