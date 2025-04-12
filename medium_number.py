from tkinter.ttk import Combobox
from tkinter import *
import random







medium_number_list=[1,2,3,4,5,6,7,8,9,10]

def medium_number():   
    pc_medium_number=random.choice(medium_number_list)
    user_medium_number=int(combo_list_medium_number.get())
    print(f"pc: {pc_medium_number}")
    print(f"you: {user_medium_number}")
    if user_medium_number == pc_medium_number:
        win_number_medium=Toplevel()
        win_number_medium.geometry("500x500")
        win_number_medium.title("WIN")
        win_number_medium.config(bg="light green")
        lbl_win_number_medium=Label(win_number_medium,text="WIN",bg="light green",fg="green",font=("Times",20))
        lbl_pc_win_number_medium=Label(win_number_medium,text=pc_medium_number,bg="light green",fg="green",font=("Times",15))
        lbl_user_win_number_medium=Label(win_number_medium,text=user_medium_number,bg="light green",fg="green",font=("Times",15))
        lbl_win_number_medium.pack(padx=10,pady=10)
        lbl_user_win_number_medium.pack(padx=10,pady=10)
        lbl_pc_win_number_medium.pack()
    else:
        lose_number_medium=Toplevel()
        lose_number_medium.geometry("500x500")
        lose_number_medium.title("LOSE")
        lose_number_medium.config(bg="light pink")
        lbl_lose_number_medium=Label(lose_number_medium,text="LOSE",bg="light pink",fg="red",font=("Times",20))
        lbl_pc_lose_number_medium=Label(lose_number_medium,text=pc_medium_number,bg="light pink",fg="red",font=("Times",15))
        lbl_user_lose_number_medium=Label(lose_number_medium,text=user_medium_number,bg="light pink",fg="red",font=("Times",15))
        lbl_lose_number_medium.pack(padx=10,pady=10)
        lbl_pc_lose_number_medium.pack(padx=10,pady=10)
        lbl_user_lose_number_medium.pack()




#start step
root_9=Tk()
root_9.title("medium level")
root_9.geometry("450x300")
root_9.config(bg="skyblue")


#label
lbl_list_medium_number=Label(root_9,text=medium_number_list,bg="skyblue",font=("Times",15))

#spinbox
combo_list_medium_number=Combobox(root_9,value=[1,2,3,4,5,6,7,8,9,10],font=("Times",15))

#button
btn_guess_medium_number=Button(root_9,text="guess",bg="green",font=("Times",15),command=medium_number)

#packs
lbl_list_medium_number.pack(padx=10,pady=10)
combo_list_medium_number.pack(padx=10,pady=10)
btn_guess_medium_number.pack()

root_9.mainloop()