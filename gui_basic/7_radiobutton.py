from tkinter import *

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

Label(root,text="메뉴를 선택하세여").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root,text="ham", value =1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root,text="cheez", value =2, variable=burger_var)
btn_burger3 = Radiobutton(root,text="chicken", value =3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

drink_var = StringVar()
drink_1= Radiobutton(root,text="cola",value="coke",variable=drink_var)
drink_2= Radiobutton(root,text="cida",value="co2",variable=drink_var)
drink_3= Radiobutton(root,text="hwan",value="hwa",variable=drink_var)

drink_1.pack()
drink_2.pack()
drink_3.pack()


def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root,text="click", command=btncmd)
btn.pack()

root.mainloop() #계속 돌아가 ~ ! 