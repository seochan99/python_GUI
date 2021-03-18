from tkinter import *

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

listbox = Listbox(root,selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1,"딸기")
listbox.insert(END,"희찬")
listbox.pack()

def btncmd():
    #delete
    # listbox.delete(0)
    # pass 

    # 갯수 확인
    # print("list is ... ",listbox.size(), "개가 있음!")

    # 항목 확인
    print("1번째 부터 3번쪠 까지의 항목 : ",listbox.get(0,2))

    #선택된 항목 확인(위치로 반환 0,1,2,//..)
    print("선택된 항목 : ",listbox.curselection())


btn = Button(root,text="click", command=btncmd)
btn.pack()

root.mainloop() #계속 돌아가 ~ ! 