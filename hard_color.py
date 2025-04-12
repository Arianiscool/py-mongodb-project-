from tkinter import *
from tkinter.ttk import Combobox
import random







hard_color_list=["red", "blue","green", "yellow", "gold", "brown", "purple", "pink", "white", "black", "violet", "cyan"]
def hard_color():   
    pc_hard_color=random.choice(hard_color_list)
    user_hard_color=combo_list_hard_color.get()
    print(f"pc: {pc_hard_color}")
    print(f"you: {user_hard_color}")
    if user_hard_color == pc_hard_color:
        win_color_hard=Toplevel()
        win_color_hard.geometry("500x500")
        win_color_hard.title("WIN")
        win_color_hard.config(bg="light green")
        lbl_win_color_hard=Label(win_color_hard,text="WIN",bg="light green",fg="green",font=("Times",20))
        lbl_pc_win_color_hard=Label(win_color_hard,text=pc_hard_color,bg="light green",fg="green",font=("Times",15))
        lbl_user_win_color_hard=Label(win_color_hard,text=user_hard_color,bg="light green",fg="green",font=("Times",15))
        lbl_win_color_hard.pack(padx=10,pady=10)
        lbl_user_win_color_hard.pack(padx=10,pady=10)
        lbl_pc_win_color_hard.pack()
    else:
        lose_color_hard=Toplevel()
        lose_color_hard.geometry("500x500")
        lose_color_hard.title("LOSE")
        lose_color_hard.config(bg="light pink")
        lbl_lose_color_hard=Label(lose_color_hard,text="LOSE",bg="light pink",fg="red",font=("Times",20))
        lbl_pc_lose_color_hard=Label(lose_color_hard,text=pc_hard_color,bg="light pink",fg="red",font=("Times",15))
        lbl_user_lose_color_hard=Label(lose_color_hard,text=user_hard_color,bg="light pink",fg="red",font=("Times",15))
        lbl_lose_color_hard.pack(padx=10,pady=10)
        lbl_pc_lose_color_hard.pack(padx=10,pady=10)
        lbl_user_lose_color_hard.pack()




#start step
root_6=Tk()
root_6.title("hard level")
root_6.geometry("600x300")
root_6.config(bg="skyblue")

#label
lbl_list_hard_color=Label(root_6,text=hard_color_list,bg="skyblue",font=("Times",15))

#combobox
combo_list_hard_color=Combobox(root_6,value=["red","blue","green","yellow","gold","brown","purple","pink","white","black","violet","cyan"],font=("Times",15))

#button
btn_guess_hard_color=Button(root_6,text="guess",bg="green",font=("Times",15),command=hard_color)

#packs
lbl_list_hard_color.pack(padx=10,pady=10)
combo_list_hard_color.pack(padx=10,pady=10)
btn_guess_hard_color.pack()

root_6.mainloop()