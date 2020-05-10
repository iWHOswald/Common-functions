from os import path
import tkinter as tk
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import seaborn as sns
from scraper_gs import *
import re
from bs4 import BeautifulSoup


# python 3 app
class IoPlot(tk.Tk):   # IoPlot will inherit attributes from the tkinter module. the (tk.TK) is not technically necesary


    def __init__(self, *args, **kwargs):  # this is here to always load the following. always run when IoPlot is called
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default='terpylyticsicon.ico')
        tk.Tk.wm_title(self, "XX V 0.1")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)

        menubar = tk.Menu(container)
        helpmenu = Menu(menubar, tearoff=0)
        helpmsg = str("XX")
        aboutmsg = str("XX V. 0.1." '\n' "Coded in Python 3 by Iain W. H. Oswald, PhD." '\n' "Github: https://github.com/iWHOswald/")
        abouttitle = str("About XX")
        helptitle = str("Help")
        helpmenu.add_command(label="Help", command=lambda: IoPlot.pophelpmsg(self, helpmsg, helptitle))
        helpmenu.add_command(label="About...", command= lambda: IoPlot.pophelpmsg(self, aboutmsg, abouttitle))
        menubar.add_cascade(label="Help", menu=helpmenu)

        tk.Tk.config(self, menu=menubar)


        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame

        frame.grid(row=10, column=10, sticky="nsew")
        self.show_frame(StartPage)

    def pophelpmsg(self, data, poptitle):
        gridcounter = 0
        popup = tk.Tk()
        popup.wm_title(poptitle)
        #popup.resizable(width=500, height=500)
        S = tk.Scrollbar(popup)
        T = tk.Text(popup, width=60)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        T.pack()
        T.insert(tk.END, data)

        popup.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        #  lots of stuff to set to 0 to initialize. this makes sure different files don't overwrite each other
        self.UnkownCount = 0
        rowCounter = 0

        #  this initializes the gui
        tk.Frame.__init__(self, parent)

        open_button = ttk.Button(self, text="Open GCxGC CSV file",command=lambda: print("fill"))
        open_button.grid(sticky=NW, row=rowCounter, column=0, pady=4, padx=4)
        open_SCD_button = ttk.Button(self, text="View GF Data",command=lambda: print("fill"))
        open_SCD_button.grid(sticky=NW, row=rowCounter, column=1, pady=4, padx=4)
        self.StrainManager = ttk.Button(self, text="Open Strain Manager",command=lambda: print("fill"))
        self.StrainManager.grid(sticky=NW, row=rowCounter, column=2, pady=4, padx=4)
        rowCounter = rowCounter + 1

        save_xlsx_button = ttk.Button(self, text="Save to excel (all)",command=lambda: print("fill"))
        save_xlsx_button.grid(sticky=NW, row=rowCounter, column=0, pady=4, padx=4)
        rowCounter = rowCounter + 1
        import_db_button = ttk.Button(self, text="View Analytics",
                                      command=lambda:print("fill") )
        save_GCpdf_button = ttk.Button(self, text="Save to GC COA PDF",command=lambda: print("fill"))
        save_GCpdf_button.grid(sticky=NW, row=rowCounter, column=0, pady=4, padx=4)
        rowCounter = rowCounter + 1


app = IoPlot()
app.geometry("450x600")
app.resizable(width=False, height=False)
app.mainloop()
