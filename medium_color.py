from tkinter.ttk import Combobox
from tkinter import *
import random







medium_color_list=["red","blue","green","yellow","orange","purple"]
def medium_color():   
    pc_medium_color=random.choice(medium_color_list)
    user_medium_color=combo_list_medium_color.get()
    print(f"pc: {pc_medium_color}")
    print(f"you: {user_medium_color}")
    if user_medium_color == pc_medium_color:
        win_color_medium=Toplevel()
        win_color_medium.geometry("500x500")
        win_color_medium.title("WIN")
        win_color_medium.config(bg="light green")
        lbl_win_color_medium=Label(win_color_medium,text="WIN",bg="light green",fg="green",font=("Times",20))
        lbl_pc_win_color_medium=Label(win_color_medium,text=pc_medium_color,bg="light green",fg="green",font=("Times",15))
        lbl_user_win_color_medium=Label(win_color_medium,text=user_medium_color,bg="light green",fg="green",font=("Times",15))
        lbl_win_color_medium.pack(padx=10,pady=10)
        lbl_user_win_color_medium.pack(padx=10,pady=10)
        lbl_pc_win_color_medium.pack()
    else:
        lose_color_medium=Toplevel()
        lose_color_medium.geometry("500x500")
        lose_color_medium.title("LOSE")
        lose_color_medium.config(bg="light pink")
        lbl_lose_color_medium=Label(lose_color_medium,text="LOSE",bg="light pink",fg="red",font=("Times",20))
        lbl_pc_lose_color_medium=Label(lose_color_medium,text=pc_medium_color,bg="light pink",fg="red",font=("Times",15))
        lbl_user_lose_color_medium=Label(lose_color_medium,text=user_medium_color,bg="light pink",fg="red",font=("Times",15))
        lbl_lose_color_medium.pack(padx=10,pady=10)
        lbl_pc_lose_color_medium.pack(padx=10,pady=10)
        lbl_user_lose_color_medium.pack()




#start step
root_5=Tk()
root_5.title("medium level")
root_5.geometry("450x300")
root_5.config(bg="skyblue")

#label
lbl_list_medium_color=Label(root_5,text=medium_color_list,bg="skyblue",font=("Times",15))

#combobox
combo_list_medium_color=Combobox(root_5,value=["red","blue","green","yellow","orange","purple"],font=("Times",15))

#button
btn_guess_medium_color=Button(root_5,text="guess",bg="green",font=("Times",15),command=medium_color)

#packs
lbl_list_medium_color.pack(padx=10,pady=10)
combo_list_medium_color.pack(padx=10,pady=10)
btn_guess_medium_color.pack()

root_5.mainloop()