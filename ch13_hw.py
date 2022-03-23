import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x500')
        self.main_window.title('Pizza Order')

############## FRAMES ##############
        self.frame0 = tkinter.Frame(self.main_window)
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame0.pack(side='top')
        self.frame1.pack(side='top')
        self.frame2.pack(side='top')
        self.frame3.pack(side='top')
        self.frame4.pack(side='top')
        self.frame5.pack(side='top')
####### INPUT BOX ########
        self.fname_label = tkinter.Label(self.frame1, text = 'First Name')
        self.fname_entry =tkinter.Entry(self.frame1,width=10)
        self.fname_label.pack(side='left')
        self.fname_entry.pack(side= 'left')
        self.lname_label = tkinter.Label(self.frame1, text = 'Last Name')
        self.lname_entry =tkinter.Entry(self.frame1,width=10)
        self.lname_label.pack(side='left')
        self.lname_entry.pack(side= 'left')

############ CHECK BOXES ############
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()

        self.cb_var3.set(.5)
        self.cb_var1.set(.5)
        self.cb_var2.set(.5)
        self.cb_var4.set(.5)


        self.cb1 = tkinter.Checkbutton(self.frame2, text= "Pepperoni", variable= self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.frame2, text= "Mushrooms", variable= self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.frame2, text= "Ham", variable= self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.frame2, text= "Sausage", variable= self.cb_var4)
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
####### RADIO BUTTONS ########

####### LABELS ########
        self.welcome_label = tkinter.Label(self.frame0, text = "Welcome to Hal's Pizzaria")
        self.welcome_label.pack()
###### BUTTONS ########

        self.mybutton = tkinter.Button(self.main_window, text = 'Review Order', command= self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text='Submit', command= self.main_window.destroy)
        self.mybutton.pack(side= 'left')
        self.quit_button.pack(side='right')


        
        tkinter.mainloop()
    
    def do_something(self):
        self.message = "you have selected: \n"
        
        if self.cb_var1.get() == 1:
            self.message += '1\n'
        if self.cb_var2.get() == 1:
            self.message += '2\n'
        if self.cb_var3.get() == 1:
            self.message += '3\n'
        
        tkinter.messagebox.showinfo("response", self.message)

my_gui = MyGUI()
print ("Moving on")

