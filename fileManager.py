from  Tkinter import *
from ttk import *
import tkFileDialog
import tkMessageBox
import os
import shutil
import datetime
import time


WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def openDirectoryContent():
    _path = tkFileDialog.askdirectory(initialdir=WORKING_DIRECTORY)
    path = next(os.walk(_path))[0]
    dirs = next(os.walk(_path))[1]
    files = next(os.walk(_path))[2]

    i = 1
    line = ""
    text = Text(root)
    text.insert(INSERT, "\n =============::PATH ::========== \n")
    text.insert(END, path)
    text.insert(END, "\n =============::DIRECTORY::========== \n")
    text.insert(END, dirs)
    text.insert(END, "\n =============:: FILES::==============  \n")
    text.insert(END, "\n File Name " + "\t" + "Creation_Time" + "\t" + "Last_Modification")
    for f in files:
        stat = os.stat(_path+'\\'+ f)
        line = "s\n" + f  + ","+ time.ctime(stat.st_ctime) + "," + time.ctime(stat.st_mtime)
        text.insert(END, line)
        i = i + 1
    text.pack()

def readFile():
   text = Text(root)
   text.pack(expand=YES, fill=BOTH)
   the_file = tkFileDialog.askopenfile(mode='r')
   text.insert(0.0, the_file.read())

def copyFile():

    _src = tkFileDialog.askopenfilename(initialdir=WORKING_DIRECTORY)
    _dst = tkFileDialog.askdirectory(initialdir=WORKING_DIRECTORY)
    try:
        shutil.copy(_src, _dst)
        tkMessageBox.showinfo("Message","Copy Done Successfully")
    except IOError, e:
        print "Unable to copy file. %s" % e
        tkMessageBox.showerror("Message","Unable to copy file. %s" % e)

def renameMoveFile():

    def _move():
        dst = tkFileDialog.askdirectory(initialdir=WORKING_DIRECTORY)
        try:
            shutil.move(src, dst)
            tkMessageBox.showinfo("Message","File Move Successfully")
        except IOError, e:
            tkMessageBox.showerror("Message", "Unable to Move file. %s" % e)

    def _rename():
        dst = os.path.dirname(os.path.abspath(src)) + "\\" + newFilename.get()
        try:
            shutil.move(src, dst)
            tkMessageBox.showinfo("Message","Rename Done Successfully")
        except IOError, e:
            tkMessageBox.showerror("Message", "Unable to Rename file. %s" % e)

    src = tkFileDialog.askopenfilename(initialdir=WORKING_DIRECTORY)
    rootMove = Tk()

    newFilename = Entry(rootMove)
    newFilename.grid(column=1, row=0, sticky=(W, E))
    Label(rootMove, text='Rename').grid(column=2, row=0, sticky=(W, E))

    Button(rootMove, text="Move", command=_move).grid(column=1, row=2, sticky=(W, E))
    Button(rootMove, text='Rename', command=_rename).grid(column=2, row=2, sticky=(W, E))

def delFileDir ():

    def _delDir() :
        _path = tkFileDialog.askdirectory(initialdir=WORKING_DIRECTORY)
        if os.path.isdir(_path):
            shutil.rmtree(_path)

    def _delFile():
        _path = tkFileDialog.askopenfilename(initialdir=WORKING_DIRECTORY)
        if os.path.isfile(_path):
            try:
                os.remove(_path)
            except :
                print("Error. Please try again.")

    rootMove = Tk()
    Button(rootMove, text="Delete Directory ", command=_delDir).grid(column=1, row=2, sticky=(W, E))
    Button(rootMove, text='Delete File', command=_delFile).grid(column=2, row=2, sticky=(W, E))


def makeDir():
    savedir = tkFileDialog.askdirectory(title='Select folder to save results')
    tkMessageBox.showinfo("Message", "Directory Created Successfully")
    print savedir


if __name__ == "__main__":
    root = Tk()
    root.title('File Manger ..')
    mainframe = Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(side="top", fill="both", expand=True)

    photo = PhotoImage(file='Fling Cartoon.gif')
    T = Text(root, height=20, width=50)
    T.insert(INSERT, "-:: File Manager ::- ")
    T.image_create(END, image=photo)
    T.pack()
    # Create Four Button
    Button(mainframe, text="Open Directory",command = openDirectoryContent).grid(column=1, row=1, sticky=(W, E))
    Button(mainframe,text= "Browse",command=readFile).grid(column = 2 , row = 1 , sticky = ( W , E  ))
    Button(mainframe,text= "Copy",command=copyFile).grid(column = 3 , row = 1 , sticky = ( W , E  ))
    Button(mainframe, text="Rename/Move",command = renameMoveFile ).grid(column=1, row=2, sticky=(W, E))
    Button(mainframe, text="Delete", command = delFileDir ).grid(column=2, row=2, sticky=(W, E))
    Button(mainframe, text="Mkdir", command = makeDir ).grid(column=3, row=2, sticky=(W, E))
    Button(mainframe, text='Quit', command=mainframe.quit).grid(column = 4 , row = 2 , sticky = ( W , E  ))

    root.mainloop()