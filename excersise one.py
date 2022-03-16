import tkinter
import tkinter.messagebox


class Kilo_Converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Student Test Average')
        self.main_window.configure(bg='green')

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)

        self.prompt1_label = tkinter.Label(self.frame1, text = 'Enter the score for test 1:')
        self.avg1_entry =tkinter.Entry(self.frame1,width=10)
        self.prompt2_label = tkinter.Label(self.frame2, text = 'Enter the score for test 2:')
        self.avg2_entry =tkinter.Entry(self.frame2,width=10)
        self.prompt3_label = tkinter.Label(self.frame3, text = 'Enter the score for test 3:')
        self.avg3_entry =tkinter.Entry(self.frame3,width=10)

        self.average_label = tkinter.Label(self.frame4, text='Average')

        self.prompt1_label.pack(side = 'left')
        self.avg1_entry.pack(side= 'left')
        self.prompt2_label.pack(side = 'left')
        self.avg2_entry.pack(side= 'left')
        self.prompt3_label.pack(side = 'left')
        self.avg3_entry.pack(side= 'left')

        self.average_label.pack(side='left')


        self.frame1.pack(side='top')
        self.frame2.pack(side='top')
        self.frame3.pack(side='top')
        self.frame4.pack(side='top')
        self.frame5.pack(side='top')


        self.calcbutton = tkinter.Button(self.frame5, text = 'Average', command= self.convert)
        self.quit_button = tkinter.Button(self.frame5, text='Quit', command= self.main_window.destroy)

        self.calcbutton.pack(side= 'left')
        self.quit_button.pack(side='right')


        
        tkinter.mainloop()
    
    def convert(self):
        avg_score_1 = float(self.avg1_entry.get())
        avg_score_2 = float(self.avg2_entry.get())
        avg_score_3 = float(self.avg2_entry.get())

        total_avg = round(((avg_score_1+avg_score_2+avg_score_3)/3),2)

        self.results = tkinter.Label(self.frame4,text= str(total_avg))
        self.results.pack(side='right')
        


kilo_con = Kilo_Converter()


