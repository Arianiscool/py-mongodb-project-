from tkinter import *
from tkinter.ttk import Combobox


    


def color():
    level_color_info=ent_color_level.get()
    if level_color_info == "easy":
        import easy_color
    elif level_color_info == "medium":
        import medium_color
    elif level_color_info == "hard":
        import hard_color
    elif level_color_info == "insane":
        import insane_color
        
    

#start step
root_3=Tk()
root_3.title("color guess")
root_3.geometry("450x300")
root_3.config(bg="skyblue")




#label
lbl_1_level=Label(root_3,text="level: ",bg="skyblue",font=("Times",15))

#combobox
ent_color_level=Combobox(root_3,values=["easy","medium","hard","insane"],font=("Times",15))



#button
btn_play_color=Button(root_3,text="play",bg="skyblue",width=5,height=1,font=("Times",15),command=color)

#packs
lbl_1_level.pack(padx=10,pady=10)
ent_color_level.pack(padx=10,pady=10)
btn_play_color.pack()


#mainlooentp
root_3.mainloop()