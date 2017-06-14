#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.6.1
#
# Author:       Reis Mahnic
#
# Purpose:      Moves recently edited files from one folder to another. Also displays last moved date and time.
#              
#
# Tested OS:  This code was written and tested to work with Windows 10.

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3
import shutil
import datetime as dt
from tkinter.filedialog import askdirectory
from tkinter import filedialog
import datetime
from datetime import datetime, timedelta

# Be sure to import our other modules 
# so we can have access to them
import UIForFileMovement



#create database
def create_db(self):
    conn = sqlite3.connect('db_transferLog.db')
    displayLast(self)
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists tbl_transferLog(ID INTEGER PRIMARY KEY AUTOINCREMENT,col_logTime TEXT);")
    conn.commit()
    conn.close()
    count_records()
##    first_run(self)
##
##def first_run(self):
##    conn = sqlite3.connect('db_transferLog.db')
##    cur = conn.cursor()
##    cur,count = count_records(cur)
##    if count < 1:
##        cur.execute("""INSERT INTO tbl_transferLog (col_logTime) VALUES (?)""", ('08/06/17 19-09',))
##        conn.commit()
##    conn.close()

def count_records():
    conn = sqlite3.connect('db_transferLog.db')
    cur = conn.cursor()
    count = ""
    count = cur.execute("""SELECT COUNT(*) FROM tbl_transferLog""").fetchone()
    if count == None:
        conn.close()
        return ("No previous data.")
    return count[0]

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def selectSourceDirectory(self):
    source = filedialog.askdirectory()
    self.sourceReturn.set(source)
def selectDestinationDirectory(self):
    destination = filedialog.askdirectory()
    self.destinationReturn.set(destination)
def setFileSource(self):
    #List the source folder and destination folder
    source = self.sourceReturn.get()
    destination = self.destinationReturn.get()
    print(source)
    print(destination)

    #Define the current time and the time period we want to look back at
    now = dt.datetime.now()
    before = now - dt.timedelta(hours=24)

    #Print the list of file names
    files = os.listdir(source)
    addToList(self)
    displayLast(self)
    for root,dirs,files in os.walk(source):
        for file_name in files:
            path = os.path.join(root,file_name)
            st = os.stat(path)    
            mod_time = dt.datetime.fromtimestamp(st.st_mtime)
            if mod_time > before:
                #Move all files in Folder A to Folder B
                shutil.move(os.path.join(root, file_name), destination)


def addToList(self):
    conn = sqlite3.connect('db_transferLog.db')
    cur = conn.cursor()
    var_logTime = dt.datetime.now()
    cur.execute("""INSERT INTO tbl_transferLog (col_logTime) VALUES (?)""", (str((var_logTime)),))
    conn.commit()
    print(var_logTime)

def displayLast(self):
    conn = sqlite3.connect('db_transferLog.db')
    cur = conn.cursor()
    cur.execute("""SELECT col_logTime FROM tbl_transferLog WHERE ID = (SELECT MAX(ID) FROM tbl_transferLog);""")
    varLastTime = cur.fetchall()    
    for data in varLastTime:
        self.lbl_lastUse.config(text = 'Last Run: ' + (str(varLastTime[0])))
        print(str(varLastTime))
