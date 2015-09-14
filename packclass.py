from Tkinter import *
"""
Pack este cel mai usor de utilizat manager de layout, acesta aplica un
layout unul langa altul intr-un sir sau o coloana.
Eticheta = proprietate:
    text = "Textul afisat in componenta"

    pack(fill=X)- unple eticheta 
"""

class PackClass(Frame):
    def __init__(self, parent, *args, **kargs):
        Frame.__init__(self, parent, *args, **kargs)
        self.parent=parent

        self.eticheta=Label(self, text="Eticheta", bg="green", fg="black")
        self.eticheta.pack(fill=X, padx=10, pady=10, ipadx=10)

        self.listBox = Listbox()
        self.listBox.pack()

        self.quitBtn = Button(self, text="Close", command=self.quit)
        self.quitBtn.pack(ipadx=10, ipady=10)

if __name__ == "__main__":
    root = Tk()
    PackClass(root).pack(fill=BOTH)
    root.mainloop()
    root.destroy()
