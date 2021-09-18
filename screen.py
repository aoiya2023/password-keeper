# This file displays the main screen of the app
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox
from tkinter import simpledialog

import func
import data
import crypt_gp
import crypt_ac

# This function is used to check if this module was imported correctly or not.
def works():
    return True

unlocked = False  # To check if this session is unlocked or not, by default it is not (False)

# displays the main scrren.
def showWindow():
    global pwordE
    global roots

    roots = Tk()  # This creates a blank window.
    roots.title('Password Keeper')
    window_height = "400" if data.countAccounts() == -1 else str(400 + (data.countAccounts() * 35))
    roots.geometry('580x'+window_height)
    roots.resizable(0,0)

    menubar = tk.Menu(roots)
    roots.config(menu=menubar)

    settingsMenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=settingsMenu)
    settingsMenu.add_command(label="About", command=about)
    settingsMenu.add_separator()
    settingsMenu.add_command(label="Exit", command=exitWindow)

    # Row 1
    # Title
    title = Label(roots, text='Password Keeper', font="Helvetica 20 bold")
    title.grid(row=0, column=0, columnspan=3, sticky=W)


    # Row 2 is reserved for unlocked session notice.
    if not unlocked:
        gapL = Label(roots, text='\n', fg="red")
        gapL.grid(row=2, column=0, sticky=W, columnspan=3)
    else:
        unlockedL = Label(roots, text='Session Unlocked: Information is not secure.\n', fg="red")
        unlockedL.grid(row=2, column=0, sticky=W, columnspan=3)
    # Row 3
    availActionsL = Label(roots, text='Available Actions:')
    availActionsL.grid(row=3, column=0, sticky=W)

    """
    refreshBtn = Button(roots, text='Refresh', command=refreshWindow)
    refreshBtn.grid(row=3, column=1, sticky=E, padx=5)
    """

    # Main Buttons - Delete All, Add Entry
    if d.countAccounts() > 0:
        deleteAllBtn = Button(roots, text='Delete All', fg='red', command=confirmDeleteAll)
        deleteAllBtn.grid(row=3, column=2, sticky=E, padx=5)
        addEntryBtn = Button(roots, text='Add Entry', command=addEntry)
        addEntryBtn.grid(row=3, column=4, sticky=E, padx=5)
    else:
        addEntryBtn = Button(roots, text='Add Entry', command=addEntry)
        addEntryBtn.grid(row=3, column=2, sticky=E, padx=45)
    if unlocked:
        lockBtn = Button(roots, text='Lock Session', command=lockSession)
        lockBtn.grid(row=3, column=3, sticky=E, padx=5)
    else:
        unlockBtn = Button(roots, text='Unlock Session', command=unlockSession)
        unlockBtn.grid(row=3, column=3, sticky=E, padx=5)

    myaccL = Label(roots, text='\nMy Accounts', font="Helvetica 12 bold")
    myaccL.grid(row=4, column=0, sticky=W, columnspan=3)

    # Row 3
    if d.countAccounts() == 0:
        nodataL = Label(roots, text='\nNo accounts found. Click on Add Entry above to add a new account.')
        nodataL.grid(row=5, column=0, sticky=W, columnspan=3)
    elif d.countAccounts() == -1:
        errorL = Label(roots, text='\nThere was an error fetching the data.',fg="red")
        errorL.grid(row=5, column=0, sticky=W, columnspan=3)
    else:
        displayAccounts()

    roots.mainloop()  # This just makes the window keep open, we will destroy it soon

# This function destroys the window, and reopens it to refresh the data.
def refreshWindow():
    f.Log("Window has been refreshed.", "refreshWindow")
    roots.destroy()
    showWindow()


# This function opens the Add New Entry window.
def addEntry():
    global entryWindow
    global nameE
    global unameE
    global passE
    global gapL
    entryWindow = Tk()
    entryWindow.title('New Account')
    entryWindow.geometry('350x250')
    entryWindow.resizable(0,0)
    title = Label(entryWindow, text='Enter New Account Details\n', font="Helvetica 15 bold")
    title.grid(row=0, column=0, columnspan=3, sticky=W)
    nameL = Label(entryWindow, text='Account Name: ')
    nameL.grid(row=1, column=0, sticky=W)
    nameE = Entry(entryWindow)
    nameE.grid(row=1, column=1)
    unameL = Label(entryWindow, text='Username: ')
    unameL.grid(row=2, column=0, sticky=W)
    unameE = Entry(entryWindow)
    unameE.grid(row=2, column=1)
    passL = Label(entryWindow, text='Password: ')
    passL.grid(row=3, column=0, sticky=W)
    passE = Entry(entryWindow, show='*')
    passE.grid(row=3, column=1)
    gapL = Label(entryWindow, text='\n')
    gapL.grid(row=4, column=0, columnspan=2, sticky=W)
    entryBtn = Button(entryWindow, text='Add New Account', fg='green', command=addEntryHandler)
    entryBtn.grid(row=5, column=1, columnspan=2, sticky=E)


# This function is used to check if all the fields are checked or not
def addEntryHandler():
    name = nameE.get()
    uname = unameE.get()
    pwd = passE.get()
    if name == "" or uname == "" or pwd == "":
        gapL.config(text='\nPlease enter all the fields.\n', fg='red')
    else:
        if d.addEntry(name, uname, pwd):
            gapL.config(text='\nSuccess!\n', fg='green')
            entryWindow.destroy()
            refreshWindow()
        else:
            gapL.config(text='\nThere was an error.\n', fg='red')
