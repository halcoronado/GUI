import tkinter
import tkinter.messagebox


class Kilo_Converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo 2')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')        
        
        self.radio_var = tkinter.IntVar()

        ##Set the default button
        

        self.rb1 = tkinter.Radiobutton(self.top_frame, text= 'Option 1' , 
                                        variable = self.radio_var, value=10)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text= 'Option 2' , 
                                        variable = self.radio_var, value=20)
        
        self.rb3 = tkinter.Radiobutton(self.top_frame, text= 'Option 3' , 
                                        variable = self.radio_var, value=30)
        self.rb2.select()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.okaybutton = tkinter.Button(self.bottom_frame, text = 'Okay', command= self.show_choice)
        self.reset_buton = tkinter.Button(self.bottom_frame, text = 'Reset', command= self.rb1.select)
        self.quitbutton = tkinter.Button(self.main_window, text='Quit', command= self.main_window.destroy)

        self.okaybutton.pack(side='left')
        self.reset_buton.pack(side='left')
        self.quitbutton.pack(side='left')
        tkinter.mainloop()
    
    def show_choice(self):
        tkinter.messagebox.showinfo('Selection', "You hace selected option"+ str(self.radio_var.get()))

kilo_con = Kilo_Converter()


