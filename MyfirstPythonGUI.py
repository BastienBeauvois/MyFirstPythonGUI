import tkinter as tk
from random import randrange
from functools import partial



class MyFirstPythonGUI:


    def __init__(self):
    #constants in the class
        self.FontSize = 22
        self.FontSize_btn = 36
    
        self.window=tk.Tk()
        self.window.title('MyFirstPythonGUI')
        self.window.geometry('{}x{}'.format(1400, 1000))
    
    def main(self):
        self.CreateMainContainers()
        self.LayoutMainContainers()
        self.SplitCentreFrame()

        self.PopulateTopFrame()
        self.PopulateBottomFrame()
        self.PopulateKeyboard()


        self.window.mainloop()


    def CreateMainContainers(self):
        self.top_frame = tk.Frame(self.window, bg='yellow', width=1400, height=300, pady=3)
        self.center_frame = tk.Frame(self.window, bg='blue', pady=3) #, relief=tk.RAISED, borderwidth=1)
        self.btm_frame = tk.Frame(self.window, bg='red', width=1400, height=300, pady=3)


    def LayoutMainContainers(self):
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.top_frame.grid(row=0, sticky="ew")
        self.center_frame.grid(row=1, sticky="nsew")
        self.btm_frame.grid(row=4, sticky="ew")        


    def PopulateTopFrame(self):
        self.top_frame.grid_rowconfigure(0, weight=1, minsize=50)
        self.top_frame.grid_columnconfigure(0, weight=1, minsize=75)

        # create the widgets for the top frame
        self.top_label = tk.Label(self.top_frame, text='9-DIGIT KEYPAD', bg="black", fg="white", height=4, font=("Courier", self.FontSize))
        # layout the widgets in the top frame
        self.top_label.grid(row=0, columnspan=1, sticky="nsew")

        #randomly generetae a sequence of 4 digits
        NumberOfDigits=4

        pin_str=''
        for i in range(NumberOfDigits):
            pin_str=pin_str + str(randrange(1,10,1))

        # create the widgets for the top frame
        self.top_label2 = tk.Label(self.top_frame, text='Enter the following 4-digit code : '+ pin_str, bg="black", fg="white", height=4, font=("Courier", self.FontSize))
        # layout the widgets in the top frame
        self.top_label2.grid(row=1, columnspan=1, sticky="nsew")


    def PopulateBottomFrame(self):
        self.btm_frame.grid_rowconfigure(0, weight=1)
        self.btm_frame.grid_columnconfigure(0, weight=1)


        # create the widgets for the top frame
        self.btm_label1 = tk.Label(self.btm_frame, text='Your entry:', width=1, height=1, font=("Courier", self.FontSize), bg='black', fg='white')
        # layout the widgets in the top frame
        self.btm_label1.grid(row=0, columnspan=1, sticky="nsew")

        YourPin_str = '_ _ _ _'
        
        # create the widgets for the top frame
        self.btm_label2 = tk.Label(self.btm_frame, text=YourPin_str, bg="black", fg="white", height=4, font=("Courier", self.FontSize))
        # layout the widgets in the top frame
        self.btm_label2.grid(row=1, columnspan=1, sticky="nsew")


    def SplitCentreFrame(self):
        self.center_frame.grid_rowconfigure(0, weight=1)
        self.center_frame.grid_columnconfigure(1, weight=1)


        self.ctr_left = tk.Frame(self.center_frame, bg='green', width=400)
        self.ctr_mid = tk.Frame(self.center_frame, bg='cyan')
        self.ctr_right = tk.Frame(self.center_frame, bg='orange', width=400)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.ctr_mid.grid(row=0, column=1, sticky="nsew")
        self.ctr_right.grid(row=0, column=2, sticky="ns")


    def PopulateKeyboard(self):

        def handle_click(buttonId):
        #    print("The button was clicked! event", str(event))
            print("The button was clicked!", str(buttonId))
            return;


        Btn_id=1
        for i in range(3):
            self.ctr_mid.grid_rowconfigure(i, weight=1, minsize=50)
            self.ctr_mid.grid_columnconfigure(i, weight=1, minsize=75)

            for j in range(3):
                frame = tk.Frame(master=self.ctr_mid, relief=tk.RAISED, borderwidth=1)
                frame.grid(row=i, column=j, padx=5, pady=5)
                button = tk.Button(master=frame, text=f"{Btn_id}", width=5, height=5, font=("Courier", self.FontSize_btn), command=partial(handle_click,Btn_id) )
                button.pack(padx=5, pady=5) 
                Btn_id = Btn_id + 1



if __name__ == "__main__":
    MyGUI=MyFirstPythonGUI()
    MyGUI.main()
    



