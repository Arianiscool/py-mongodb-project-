from tkinter import *
from tkinter.ttk import Combobox


    


def color():
    level_color_info=combo_number_level.get()
    if level_color_info == "easy":
        import easy_number
    elif level_color_info == "medium":
        import medium_number
    elif level_color_info == "hard":
        import hard_number
    elif level_color_info == "insane":
        import insane_number
        
    

#start step
root_12=Tk()
root_12.title("number guess")
root_12.geometry("450x300")
root_12.config(bg="skyblue")




#label
lbl_2_level=Label(root_12,text="level: ",bg="skyblue",font=("Times",15))

#combobox
combo_number_level=Combobox(root_12,values=["easy","medium","hard","insane"],font=("Times",15))



#button
btn_play_number=Button(root_12,text="play",bg="skyblue",width=5,height=1,font=("Times",15),command=color)

#packs
lbl_2_level.pack(padx=10,pady=10)
combo_number_level.pack(padx=10,pady=10)
btn_play_number.pack()


#mainlooentp
root_12.mainloop()