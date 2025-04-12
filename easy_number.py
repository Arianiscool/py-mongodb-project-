from tkinter import *
from tkinter.ttk import Combobox
import random








easy_number_list=[1,2,3]
def easy_number():   
    pc_easy_number=random.choice(easy_number_list)
    user_easy_number=int(combo_list_easy_number.get())
    print(f"pc: {pc_easy_number}")
    print(f"you: {user_easy_number}")
    if user_easy_number == pc_easy_number:
        win_number_easy=Toplevel()
        win_number_easy.geometry("500x500")
        win_number_easy.title("WIN")
        win_number_easy.config(bg="light green")
        lbl_win_number_easy=Label(win_number_easy,text="WIN",bg="light green",fg="green",font=("Times",20))
        lbl_pc_win_number_easy=Label(win_number_easy,text=pc_easy_number,bg="light green",fg="green",font=("Times",15))
        lbl_user_win_number_easy=Label(win_number_easy,text=user_easy_number,bg="light green",fg="green",font=("Times",15))
        lbl_win_number_easy.pack(padx=10,pady=10)
        lbl_user_win_number_easy.pack(padx=10,pady=10)
        lbl_pc_win_number_easy.pack()
    else:
        lose_number_easy=Toplevel()
        lose_number_easy.geometry("500x500")
        lose_number_easy.title("LOSE")
        lose_number_easy.config(bg="light pink")
        lbl_lose_number_easy=Label(lose_number_easy,text="LOSE",bg="light pink",fg="red",font=("Times",20))
        lbl_pc_lose_number_easy=Label(lose_number_easy,text=pc_easy_number,bg="light pink",fg="red",font=("Times",15))
        lbl_user_lose_number_easy=Label(lose_number_easy,text=user_easy_number,bg="light pink",fg="red",font=("Times",15))
        lbl_lose_number_easy.pack(padx=10,pady=10)
        lbl_pc_lose_number_easy.pack(padx=10,pady=10)
        lbl_user_lose_number_easy.pack()




#start step
root_8=Tk()
root_8.title("easy level")
root_8.geometry("450x300")
root_8.config(bg="skyblue")

#label
lbl_list_easy_number=Label(root_8,text=easy_number_list,bg="skyblue",font=("Times",15))

#combobox
combo_list_easy_number=Combobox(root_8,value=[1,2,3],font=("Times",15))

#button
btn_guess_easy_number=Button(root_8,text="guess",bg="green",font=("Times",15),command=easy_number)

#packs
lbl_list_easy_number.pack(padx=10,pady=10)
combo_list_easy_number.pack(padx=10,pady=10)
btn_guess_easy_number.pack()

root_8.mainloop()