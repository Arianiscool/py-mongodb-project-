from tkinter.ttk import Combobox
from tkinter import *
import random






insane_number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
def insane_number():   
    pc_insane_number=random.choice(insane_number_list)
    user_insane_number=int(combo_list_insane_number.get())
    print(f"pc: {pc_insane_number}")
    print(f"you: {user_insane_number}")
    if user_insane_number == pc_insane_number:
        win_number_insane=Toplevel()
        win_number_insane.geometry("500x500")
        win_number_insane.title("WIN")
        win_number_insane.config(bg="light green")
        lbl_win_number_insane=Label(win_number_insane,text="WIN",bg="light green",fg="green",font=("Times",20))
        lbl_pc_win_number_insane=Label(win_number_insane,text=pc_insane_number,bg="light green",fg="green",font=("Times",15))
        lbl_user_win_number_insane=Label(win_number_insane,text=user_insane_number,bg="light green",fg="green",font=("Times",15))
        lbl_win_number_insane.pack(padx=10,pady=10)
        lbl_user_win_number_insane.pack(padx=10,pady=10)
        lbl_pc_win_number_insane.pack()
        print(insane_number_list)
    else:
        lose_number_insane=Toplevel()
        lose_number_insane.geometry("500x500")
        lose_number_insane.title("LOSE")
        lose_number_insane.config(bg="light pink")
        lbl_lose_number_insane=Label(lose_number_insane,text="LOSE",bg="light pink",fg="red",font=("Times",20))
        lbl_pc_lose_number_insane=Label(lose_number_insane,text=pc_insane_number,bg="light pink",fg="red",font=("Times",15))
        lbl_user_lose_number_insane=Label(lose_number_insane,text=user_insane_number,bg="light pink",fg="red",font=("Times",15))
        lbl_lose_number_insane.pack(padx=10,pady=10)
        lbl_pc_lose_number_insane.pack(padx=10,pady=10)
        lbl_user_lose_number_insane.pack()
        print(insane_number_list)




#start step
root_11=Tk()
root_11.title("insane level")
root_11.geometry("450x300")
root_11.config(bg="skyblue")

#label
lbl_list_insane_number=Label(root_11,text="look at the terminal",bg="skyblue",font=("Times",15))

#spinbox
combo_list_insane_number=Combobox(root_11,value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],font=("Times",15))

#button
btn_guess_insane_number=Button(root_11,text="guess",bg="green",font=("Times",15),command=insane_number)

#packs
lbl_list_insane_number.pack(padx=10,pady=10)
combo_list_insane_number.pack(padx=10,pady=10)
btn_guess_insane_number.pack()




print(insane_number_list)
root_11.mainloop()