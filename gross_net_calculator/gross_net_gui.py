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
        # Hello Button
        self.hi_there = tk.Button(self)
        self.hi_there['text'] = 'Hello World\n(click me)'
        self.hi_there['command'] = self.say_hi
        self.hi_there.pack(side='top')

        # Quit Button
        self.quit = tk.Button(self, text='QUIT', fg='red', 
                              command=root.destroy)
        self.quit.pack(side='bottom')

        # Dollars input box and label
        self.dollars_label = tk.Label(self, text='Enter dollars to convert')
        self.dollars = tk.Text(self)
        self.dollars_label.pack(side='left')
        self.dollars.pack(side='right')

        # Gross Output box
        self.gross_output = tk.Label(self, text='Gross=')
        self.gross_output.pack(side='bottom')

        # Net Output box
        self.net_output = tk.Label(self, text='Net=')
        self.net_output.pack(side='bottom')


        

    def say_hi(self):
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
