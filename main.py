from tkinter import*
form tkinter import ttk 
import random
from datetime import datetime
import tkinter.messagebox


class Library:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management Systems")
        self.root.geometry("1350x750+0+0")

    #=================FRAME=========================================
   
    MainFrame = Frame(self.root)
    MainFrame.grid()

    TitleFrame = Frame(MainFrame, width = 1350, padx = 20, bd = 20, relief = RIDGE)
    TitleFrame.pack(side=TOP)
    self.lblTitle = Label(TitleFrame, width = 39, font = ('arial', 40, 'bold',), text = "\tLibrary Management Systems\t", padx = 12)
    self.lblTitle.grid()

    ButtonFrame = Frame(MainFrame, bd = 20, width = 1350, height = 50, padx = 20, relief = RIDGE)
    ButtonFrame.pack(side = BOTTOM)

    FrameDetail = Frame(MainFrame, bd = 20, width = 1350, height = 100, padx = 20, relief = RIDGE)
    FrameDetail.pack(side = BOTTOM)

    DataFrame = Frame(MainFrame, bd = 20, width = 1300, height = 400, padx = 20, relief = RIDGE)
    DataFrame.pack(side=BOTTOM)

    DataFrameLEFT = LabelFrame(DataFrame, bd = 10, width = 800, height = 300, padx = 20, relief = RIDGE, font = ('arial', 12, 'bold'), text = "Library membership Info:",)
    
    DataFrameLEFT.pack(side = LEFT)

    DataFrameRIGHT = LabelFrame(DataFrame, bd = 10, width = 450, height = 300, padx = 20, relief = RIDGE, font = ('arial', 12, 'bold'), text = "Book Details:",)
    DataFrameRIGHT.pack(side=RIGHT)

    #==========================Widget=========================================================================

    self.lblMemberType = Label(DataFrameLEFT, font = ('arial', 12, 'bold'), text = "Member Type: ", padx=2, pady=2)
    self.lblMemberType . grid(row = 0, column = 0, sticky = W)

    self.cboMemberType = ttk.Combobox(DataFrameLEFT, font =('arial', 12, 'bold'), state = 'readonly', width = 23)
    self.cboMemberType['value'] = ('','Student', 'Lecturer', 'Admin Staff')
    self.cboMemberType.current(0)
    self.cboMemberType . grid (row = 0, column = 1)


if __name__=='__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()

