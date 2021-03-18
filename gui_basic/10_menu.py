
from tkinter import *

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

def creat_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=creat_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")

menu.add_cascade(label="File", menu=menu_file)

root.config(menu=menu)

root.mainloop() #계속 돌아가 ~ ! 