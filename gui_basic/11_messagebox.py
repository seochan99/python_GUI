from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Chans GUI") #이름 
root.geometry("640x480+310+150") #가로*세로 + x좌표 +y좌표  

#기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("알림","정상적으로 예매 완료 되었습니다.")

def warn():
    msgbox.showwarning("경고","해당 좌석은 매진됐습니다.")

def error():
    msgbox.showerror("에러","결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소 ","해당 좌석은 유아동반석입니다. 예약하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("ㅇㅖ 아니오","해당 좌석은 역방향입니다. 예매할거?")

def yesnoc():
    response = msgbox.askyesnocancel(title=None,message="예매 내역이 저장되지 않았습니다. \n 저장 후 프로그램을 종료하시겠습니까 ?")
    #네 아니오 취소 True False None 
    if response == 1:
        print("네")
    elif response ==0:
        print("아니옹")
    else:
        print("cancel")
Button(root,command=info,text="알림").pack()
Button(root,command=warn,text="경고").pack()
Button(root,command=error,text="에러").pack()
Button(root,command=okcancel,text="확인 취소").pack()
Button(root,command=retrycancel,text="재시도 취소").pack()
Button(root,command=yesno,text="Yes No").pack()
Button(root,command=yesnoc,text="Yes No Cancecl").pack()





root.mainloop() #계속 돌아가 ~ ! 