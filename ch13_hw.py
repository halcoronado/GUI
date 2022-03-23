import tkinter
import tkinter.messagebox
from turtle import bgcolor


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('400x150')
        self.main_window.title('Pizza Order')
        self.main_window.configure(bg='black')

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
        self.fname_label.configure(bg='orange')
        self.fname_entry.configure(bg= 'orange')
        self.lname_label = tkinter.Label(self.frame1, text = 'Last Name')
        self.lname_entry =tkinter.Entry(self.frame1,width=10)
        self.lname_label.pack(side='left')
        self.lname_entry.pack(side= 'left')
        self.lname_label.configure(bg='orange')
        self.lname_entry.configure(bg= 'orange')

############ CHECK BOXES ############
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()

        self.cb_var3.set(0)
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var4.set(0)


        self.cb1 = tkinter.Checkbutton(self.frame2, text= "Pepperoni", variable= self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.frame2, text= "Mushrooms", variable= self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.frame2, text= "Ham", variable= self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.frame2, text= "Sausage", variable= self.cb_var4)
        self.cb1.pack(side= 'left')
        self.cb2.pack(side='left')
        self.cb3.pack(side='left')
        self.cb4.pack(side='left')
        self.cb1.configure(bg= 'yellow')
        self.cb2.configure(bg='yellow')
        self.cb3.configure(bg='yellow')
        self.cb4.configure(bg='yellow')       
####### RADIO BUTTONS ########
        self.radio_var = tkinter.StringVar()
        self.rb1 = tkinter.Radiobutton(self.frame3, text= 'Small' , 
                                        variable = self.radio_var, value='Small')
        self.rb2 = tkinter.Radiobutton(self.frame3, text= 'Medium' , 
                                        variable = self.radio_var, value='Medium')        
        self.rb3 = tkinter.Radiobutton(self.frame3, text= 'Large' , 
                                        variable = self.radio_var, value='Large')
        self.rb4 = tkinter.Radiobutton(self.frame3, text= 'X-Large' , 
                                        variable = self.radio_var, value='X-Large')
        self.rb2.select()
        self.rb1.pack(side='right')
        self.rb2.pack(side='right')
        self.rb3.pack(side='right')
        self.rb4.pack(side='right')
        self.rb1.configure(bg='green')
        self.rb2.configure(bg='green')
        self.rb3.configure(bg='green')
        self.rb4.configure(bg='green')
####### LABELS ########
        self.welcome_label = tkinter.Label(self.frame0, text = "Welcome to Hal's Pizzaria")
        self.welcome_label.pack()
        self.welcome_label.configure(bg= 'red')
###### BUTTONS ########

        self.mybutton = tkinter.Button(self.frame5, text = 'Review Order', command= self.do_something)
        self.quit_button = tkinter.Button(self.frame5, text='Submit', command= self.main_window.destroy)
        self.mybutton.pack(side= 'left')
        self.quit_button.pack(side='right')
        self.mybutton.configure(bg= 'blue')
        self.quit_button.configure(bg='purple')


        
        tkinter.mainloop()
    
    def do_something(self):
        self.message = "Toppings: "
        
        if self.cb_var1.get() == 1:
            self.message += 'Pepperoni '
        if self.cb_var2.get() == 1:
            self.message += 'Mushrooms '
        if self.cb_var3.get() == 1:
            self.message += 'Ham '
        if self.cb_var4.get() == 1:
            self.message += 'Sausage ' 
        self.price = '$ '

        if self.radio_var.get() == 'Small':
                self.price += '6'
        if self.radio_var.get() == 'Medium':
                self.price += '12'
        if self.radio_var.get() == 'Large':
                self.price+= '18'
        if self.radio_var.get() == 'X-Large':
                self.price+= '24'


        tkinter.messagebox.showinfo("Order Review", 'Name '+ str(self.fname_entry.get()) +' '+ 
                str(self.lname_entry.get()) + '\n'+ self.message +'\n' +"Size: "+ str(self.radio_var.get())+'\n'
                + 'Total: ' + self.price)

my_gui = MyGUI()
print ("Moving on")

