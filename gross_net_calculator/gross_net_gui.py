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

    def keypress(self, key):
        """ Handles keypresses from the input boxes
        """
        print('key={}'.format(key))
        self.calc_gross_net()

    def validate(self, newtext):
        """ Handles keypresses during the validation portion.
        """
        print('validate={}'.format(newtext))
        self.calc_gross_net()
        return True

    def create_widgets(self):

        vcmd = self.register(self.validate)
        #vcmd = app.register(self.validate)

        # Quit Button
        self.quit = tk.Button(self, text='QUIT', fg='red', 
                              command=root.destroy)
        self.quit.pack(side='bottom')

        # Input Frame
        self.input_frame = tk.Frame(self) 
        self.input_frame.pack(side='top')

        # Dollars input box label (input_frame)
        self.dollars_label = tk.Label(self.input_frame, text='Enter dollar amount to convert')
        self.dollars_label.grid(sticky='E', row=0, column=0)
        
        # Dollars input box (input_frame)
        self.dollars = tk.Entry(self.input_frame, width='20', validate='key', validatecommand=(vcmd, '%P'))
        self.dollars.grid(sticky='W', row=0, column=1)
        #self.dollars.bind('<Key>', self.keypress)

        # Fed Tax Label
        self.fed_tax_label = tk.Label(self.input_frame, text='Federal Tax Rate')
        self.fed_tax_label.grid(sticky='E', row=1, column=0)

        # Fed Tax input text box
        self.fed_tax_text = tk.Entry(self.input_frame, width='20')
        self.fed_tax_text.grid(sticky='W', row=1, column=1)
        
        # Fed Penalty Tax Label
        self.fed_penalty_tax_label = tk.Label(self.input_frame, text='Federal Tax Penalty Rate')
        self.fed_penalty_tax_label.grid(sticky='E', row=2, column=0)

        # Fed Penalty Tax input text box
        self.fed_penalty_tax_text = tk.Entry(self.input_frame, width='20')
        self.fed_penalty_tax_text.grid(sticky='W', row=2, column=1)

        # State Tax Label
        self.state_tax_label = tk.Label(self.input_frame, text='State Tax Rate')
        self.state_tax_label.grid(sticky='E', row=3, column=0)
        
        # State Tax input text box
        self.state_tax_text = tk.Entry(self.input_frame, width='20')
        self.state_tax_text.grid(sticky='W', row=3, column=1)
                
        # Calculate Button (input_frame)
        self.hi_there = tk.Button(self.input_frame)
        self.hi_there['text'] = 'Calculate Gross/Net'
        self.hi_there['command'] = self.calc_gross_net
        self.hi_there.grid()

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

        # Add text to all the grid'd text boxes
        self.dollars.insert(0, '0.00')
        self.fed_tax_text.insert(0, '0.00')
        self.fed_penalty_tax_text.insert(0, '0.00')
        self.state_tax_text.insert(0, '0.00')


    def calc_gross_net(self):
        print('hi there, everyone! The textbox says {}'.format(self.dollars.get()))
        d, f, p, s = (self.dollars.get().strip(),
                      self.fed_tax_text.get().strip(),
                      self.fed_penalty_tax_text.get().strip(),
                      self.state_tax_text.get().strip(),
                      )
        ans = gncalc(dollars=d, fed=f, state=s, penalty=p)
        #ans = gncalc(dollars=d, fed=24, state=4, penalty=0)
        print('ans={}'.format(ans))
        # self.dollars.insert('1.0', str(ans))
        self.gross_output['text'] = ans[0]
        self.net_output['text'] = ans[1]




if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    
    #vcmd = root.register(validate)
    app.mainloop()
    print('Exiting app.mainloop()')
