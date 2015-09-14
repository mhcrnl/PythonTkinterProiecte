from Tkinter import *

class Eticheta(Frame):
    def __init__(self, parent, *args, **kargs):
        Frame.__init__(self, parent, *args, **kargs)
        self.parent = parent
        
        self.initUI()

    def initUI(self):
        self.frame = Frame(self.parent, relief=GROOVE, borderwidth=2)
        
        Label(self.frame,text="Eticheta").pack()
        Button(self.frame, text="Close", command=self.quit).pack()

        self.frame.pack()



if __name__=='__main__':
    root=Tk()
    root.title("Eticheta")
    Eticheta(root, width=300, height=120).pack()
    root.mainloop()
    root.destroy()
    
