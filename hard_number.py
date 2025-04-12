from tkinter import *
from tkinter.ttk import Combobox
import random







hard_number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
def hard_number():   
    pc_hard_number=random.choice(hard_number_list)
    user_hard_number=int(combo_list_hard_number.get())
    print(f"pc: {pc_hard_number}")
    print(f"you: {user_hard_number}")
    if user_hard_number == pc_hard_number:
        win_number_hard=Toplevel()
        win_number_hard.geometry("500x500")
        win_number_hard.title("WIN")
        win_number_hard.config(bg="light green")
        lbl_win_number_hard=Label(win_number_hard,text="WIN",bg="light green",fg="green",font=("Times",20))
        lbl_pc_win_number_hard=Label(win_number_hard,text=pc_hard_number,bg="light green",fg="green",font=("Times",15))
        lbl_user_win_number_hard=Label(win_number_hard,text=user_hard_number,bg="light green",fg="green",font=("Times",15))
        lbl_win_number_hard.pack(padx=10,pady=10)
        lbl_user_win_number_hard.pack(padx=10,pady=10)
        lbl_pc_win_number_hard.pack()
    else:
        lose_number_hard=Toplevel()
        lose_number_hard.geometry("500x500")
        lose_number_hard.title("LOSE")
        lose_number_hard.config(bg="light pink")
        lbl_lose_number_hard=Label(lose_number_hard,text="LOSE",bg="light pink",fg="red",font=("Times",20))
        lbl_pc_lose_number_hard=Label(lose_number_hard,text=pc_hard_number,bg="light pink",fg="red",font=("Times",15))
        lbl_user_lose_number_hard=Label(lose_number_hard,text=user_hard_number,bg="light pink",fg="red",font=("Times",15))
        lbl_lose_number_hard.pack(padx=10,pady=10)
        lbl_pc_lose_number_hard.pack(padx=10,pady=10)
        lbl_user_lose_number_hard.pack()




#start step
root_10=Tk()
root_10.title("hard level")
root_10.geometry("680x300")
root_10.config(bg="skyblue")

#label
lbl_list_hard_number=Label(root_10,text=hard_number_list,bg="skyblue",font=("Times",15))

#combobox
combo_list_hard_number=Combobox(root_10,value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],font=("Times",15))

#button
btn_guess_hard_number=Button(root_10,text="guess",bg="green",font=("Times",15),command=hard_number)

#packs
lbl_list_hard_number.pack(padx=10,pady=10)
combo_list_hard_number.pack(padx=10,pady=10)
btn_guess_hard_number.pack()

root_10.mainloop()