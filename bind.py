from Tkinter import *

class HelloPackage:                         
    def __init__(self, parent=None):
        self.top = Frame(parent)            
        self.top.pack()
        self.data = 0
        self.make_widgets()                 
    def make_widgets(self):
        Button(self.top, text='Bye', command=self.top.quit).pack(side=LEFT)
        Button(self.top, text='Hye', command=self.message).pack(side=RIGHT)
    def message(self):
        self.data += 5
        print self.data
     
frm = Frame()
frm.pack()
Label(frm, text='hello').pack()
     
part = HelloPackage(frm)
part.top.pack(side=RIGHT) 
frm.mainloop()
frm.destroy()
