""" This is the gui module for the gross_net calculator.

"""
# TDD
# tkinter

import tkinter as tk
from gross_net_calculator import gross_net_calculator as gncalc

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Input Frame
        self.input_frame = tk.Frame(self) 
        self.input_frame.pack(side='top')
                
        
        # Calculate Button (input_frame)
        self.hi_there = tk.Button(self.input_frame)
        self.hi_there['text'] = 'Calculate Gross/Net'
        self.hi_there['command'] = self.calc_gross_net
        self.hi_there.pack(side='bottom')

        # Quit Button
        self.quit = tk.Button(self, text='QUIT', fg='red', 
                              command=root.destroy)
        self.quit.pack(side='bottom')

        # Dollars Frame
        self.dollars_frame = tk.Frame(self.input_frame)
        self.dollars_frame.pack(side='top')

        # Dollars input box label
        self.dollars_label = tk.Label(self.dollars_frame, text='Enter dollar amount to convert')
        self.dollars_label.pack(side='left')
        
        # Dollars input box
        self.dollars = tk.Text(self.dollars_frame, height='1')
        self.dollars.pack(side='right')

        # Output Frame
        self.output_frame = tk.Frame(self) 
        self.output_frame.pack(side='bottom')

        # Gross Frame
        self.gross_frame = tk.Frame(self.output_frame)
        self.gross_frame.pack(side='left')

        # Net Frame
        self.net_frame = tk.Frame(self.output_frame)
        self.net_frame.pack(side='right')
        
        # Gross Output Label
        self.gross_output_label = tk.Label(self.gross_frame, text='Gross=')
        self.gross_output_label.pack(side='top')

        # Gross Output box
        self.gross_output = tk.Label(self.gross_frame, text='Gross')
        self.gross_output.pack(side='bottom')

        # Net Output Label
        self.net_output_label = tk.Label(self.net_frame, text='Net=')
        self.net_output_label.pack(side='top')

        # Net Output box
        self.net_output = tk.Label(self.net_frame, text='Net')
        self.net_output.pack(side='bottom')


        

    def calc_gross_net(self):
        print('hi there, everyone! The textbox says {}'.format(self.dollars.get("1.0", "end")))
        ans = gncalc(self.dollars.get('1.0', 'end').strip(), 24, 4, 0)
        print('ans={}'.format(ans))
        # self.dollars.insert('1.0', str(ans))
        self.gross_output['text'] = ans[0]
        self.net_output['text'] = ans[1]



root = tk.Tk()
app = Application(master=root)
app.mainloop()
print('Exiting app.mainloop()')
