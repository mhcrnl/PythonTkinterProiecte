from Tkinter import *
"""

"""
class PackClassSir(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent=parent

        #self.createWidgets()
        self.createWidgetsWithGrid()

    def createWidgets(self):

        self.closeBtn= Button(self, text="Close", command=self.quit)
        self.saveBtn= Button(self, text="Save")
        self.openBtn= Button(self, text="Open")
        self.newBtn=Button(self, text="New")
        
        self.newBtn.pack(side=LEFT)
        self.saveBtn.pack(side=LEFT)
        self.openBtn.pack(side=LEFT)
        self.closeBtn.pack(side=LEFT)

    def createWidgetsWithGrid(self):

        culori = ['red', 'green', 'orange']
        r=0

        for c in culori:
            Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
            Entry(bg=c, relief=SUNKEN, width=10).grid(row=r, column=1)
            r=r+1

if __name__ == "__main__":
    root = Tk()
    PackClassSir(root)
    root.mainloop()
    root.destroy()
