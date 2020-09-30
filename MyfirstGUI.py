import tkinter as tk
from random import randrange
from functools import partial


FontSize=22
FontSize_btn=36
window = tk.Tk()
#window.geometry("640x380")
window.title('MyDemoGUI')
window.geometry('{}x{}'.format(1400, 1000))


# create all of the main containers
top_frame = tk.Frame(window, bg='yellow', width=1400, height=300, pady=3)
center_frame = tk.Frame(window, bg='blue', width=40, height=25, pady=3) #, relief=tk.RAISED, borderwidth=1)
btm_frame = tk.Frame(window, bg='red', width=1400, height=300, pady=3)

# layout all of the main containers
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center_frame.grid(row=1, sticky="nsew")
btm_frame.grid(row=4, sticky="ew")



#
# TOP FRAME
#

top_frame.grid_rowconfigure(0, weight=1, minsize=50)
top_frame.grid_columnconfigure(0, weight=1, minsize=75)

# create the widgets for the top frame
screen1_label = tk.Label(top_frame, text='9-DIGIT KEYPAD', bg="black", fg="white", height=4, font=("Courier", FontSize))
# layout the widgets in the top frame
screen1_label.grid(row=0, columnspan=1, sticky="nsew")


#randomly generetae a sequence of 4 digits
NumberOfDigits=4

pin_str=''
for i in range(NumberOfDigits):
	pin_str=pin_str + str(randrange(1,10,1))

print(pin_str)

# create the widgets for the top frame
screen1_label2 = tk.Label(top_frame, text='Enter the following 4-digit code:'+ pin_str, bg="black", fg="white", height=4, font=("Courier", FontSize))
# layout the widgets in the top frame
screen1_label2.grid(row=1, columnspan=1, sticky="nsew")






# create the center widgets
center_frame.grid_rowconfigure(0, weight=1)
center_frame.grid_columnconfigure(1, weight=1)


ctr_left = tk.Frame(center_frame, bg='green', width=400, height=190)
ctr_mid = tk.Frame(center_frame, bg='cyan', width=600, height=190, padx=3, pady=3)
ctr_right = tk.Frame(center_frame, bg='orange', width=400, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")



def handle_click(buttonId):
#    print("The button was clicked! event", str(event))
    print("The button was clicked!", str(buttonId))

    return;


Btn_id=1
for i in range(3):
    ctr_mid.grid_rowconfigure(i, weight=1, minsize=50)
    ctr_mid.grid_columnconfigure(i, weight=1, minsize=75)
    

    for j in range(3):
        frame = tk.Frame(master=ctr_mid, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        button = tk.Button(master=frame, text=f"{Btn_id}", width=5, height=5, font=("Courier", FontSize_btn), command=partial(handle_click,Btn_id) )
        button.pack(padx=5, pady=5)	
#        button[i, j].bind("<Button-1>", handle_click)
        Btn_id = Btn_id + 1
        


#
# BOTTOM FRAME
#

# create the center widgets

btm_frame.grid_rowconfigure(0, weight=1)
btm_frame.grid_columnconfigure(0, weight=1)


# create the widgets for the top frame
label = tk.Label(master=btm_frame, text='Your entry:', width=1, height=1, font=("Courier", FontSize), bg='black', fg='white')
# layout the widgets in the top frame
label.grid(row=0, columnspan=1, sticky="nsew")

YourPin_str='_ _ _ _'
# create the widgets for the top frame
label = tk.Label(btm_frame, text=YourPin_str, bg="black", fg="white", height=4, font=("Courier", FontSize))
# layout the widgets in the top frame
label.grid(row=1, columnspan=1, sticky="nsew")



#
# Evnet hamdler
#



window.mainloop()


