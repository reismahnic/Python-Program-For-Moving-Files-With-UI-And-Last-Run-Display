#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.6.1
#
# Author:       Reis Mahnic
#
# Purpose:      Moves recently edited files from one folder to another. Also displays last moved date and time.
#
# Tested OS:  This code was written and tested to work with Windows 10.

from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import UIForFileMovementFunc


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.sourceReturn = StringVar()
        self.destinationReturn = StringVar()

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        self.master.title("The Tkinter File Movement Program")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: UIForFileMovementFunc.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free

###########GUI STUFF###############################
        self.btn_setSource = tk.Button(self.master,width=12,height=2,text='Set Source',command=lambda: UIForFileMovementFunc.selectSourceDirectory(self))
        self.btn_setSource.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
        self.btn_setDestination = tk.Button(self.master,width=12,height=2,text='Set Destination',command=lambda: UIForFileMovementFunc.selectDestinationDirectory(self))
        self.btn_setDestination.grid(row=8,column=1,padx=(25,0),pady=(45,10),sticky=W)
        self.btn_moveFiles = tk.Button(self.master,width=12,height=2,text='Move Files',command=lambda: UIForFileMovementFunc.setFileSource(self))
        self.btn_moveFiles.grid(row=8,column=2,padx=(25,0),pady=(45,10),sticky=W)

        self.lbl_lastUse = tk.Label(self.master,text='Last Use: None')
        self.lbl_lastUse.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
            
        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: UIForFileMovementFunc.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This File Movement Program") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
       
        self.master.config(menu=menubar, borderwidth='1')

        UIForFileMovementFunc.create_db(self)
        
        
        
def main():
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
