from tkinter import Tk, Entry, Button, StringVar, Label
import re

class Calculator:
    def __init__(self, master):
        master.title('Calculator')
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Number buttons
        buttons = [
            ('7', 0, 50), ('8', 90, 50), ('9', 180, 50),
            ('4', 0, 125), ('5', 90, 125), ('6', 180, 125),
            ('1', 0, 200), ('2', 90, 200), ('3', 180, 200),
            ('0', 90, 275),
        ]

        for (text, x, y) in buttons:
            Button(master, width=11, height=4, text=text, relief='flat', bg='black', fg='white',
                   command=lambda t=text: self.show(t)).place(x=x, y=y)

        # Operation buttons
        operations = [
            ('+', 270, 50), ('-', 270, 125),
            ('*', 270, 200), ('/', 270, 275),
            ('C', 0, 275), ('=', 180, 275),
        ]

        for (text, x, y) in operations:
            if text == 'C':
                Button(master, width=11, height=4, text=text, relief='flat', bg='black', fg='white',
                       command=self.clear).place(x=x, y=y)
            elif text == '=':
                Button(master, width=11, height=4, text=text, relief='flat', bg='grey', fg='white',
                       command=self.solve).place(x=x, y=y)
            else:
                Button(master, width=11, height=4, text=text, relief='flat', bg='black', fg='white',
                       command=lambda t=text: self.show(t)).place(x=x, y=y)

        # Bind keyboard input
        master.bind('<Key>', self.key_press)

        # Label for your name
        Label(master, text='by OUABILAL', bg='gray', fg='white', font=('Arial', 10)).place(x=0, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            if re.match(r'^[\d+\-*/. ()]+$', self.entry_value):
                result = eval(self.entry_value)
                self.equation.set(result)
                self.entry_value = str(result)
            else:
                raise ValueError("Invalid Expression")
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

    def key_press(self, event):
        if event.char in '0123456789+-*/':
            self.show(event.char)
        elif event.char == '\r':  # Enter key
            self.solve()
        elif event.char == 'c' or event.char == 'C':
            self.clear()

root = Tk()
calculator = Calculator(root)
root.mainloop()
