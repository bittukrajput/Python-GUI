from tkinter import *
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def  Newfile():
    global file
    top.title("Untitled-Notepad")
    file=None
    textArea.delete(1.0 ,END)
def Openfile():
    global file
    file=askopenfilename(defaultextension=".txt",
                                  filetypes=[("All Files","*.*"),
                                      ("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        top.title(os.path.basename(file)+ "- Notepad")
        textArea.delete(1.0,END)
        f=open(file,"r")
        textArea.insert(1.0,f.read())
        f.close()
def Savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt")
        if file=="":
            file=None
        else:
            #save as new file
            f=open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()
            
            top.title(os.basename(file)+" -Notepad")
            print("File Saved")
    else:
        #file saved the file 
        f=open(file,"w")
        f.write(textArea.get(1.0,END))
            
def Exitapp():
    top.destroy()
def cut():
    textArea.event_generate(("<<Cut>>"))
def copy():
    textArea.event_generate(("<<Copy>>"))
def paste():
    textArea.event_generate(("<<Paste>>"))  
def about():
    showinfo("Notepad","Notepad created by Bittu Rajput.")
if __name__ == '__main__':
    top=Tk()
    top.title("Untitled-Notepad")
    top.geometry("644x788")
    top.iconbitmap("1.ico")
    #add text area
    textArea=Text(top,font="lucida 13 ")
    text=None
    textArea.pack(expand=True ,fill=BOTH)
    #creat menubar
    menubar=Menu(top)
    filemenu=Menu(menubar,tearoff=0)
    #to open new file
    filemenu.add_command(label="New",command=Newfile)
    #to open already existing file
    filemenu.add_command(label="Open",command=Openfile)
    #to save the  current file
    filemenu.add_command(label="Save",command=Savefile)
    filemenu.add_separator()
    #to exit the app
    filemenu.add_command(label="Exit",command=Exitapp)
    #to all commands add in file
    menubar.add_cascade(label="File",menu=filemenu)
    #top.config(menu=menubar)
    #file menu ends
    #edit menu start
    Editmenu=Menu(menubar,tearoff=0)
    #to give a fiture of cut , copy and paste
    Editmenu.add_command(label="Cut",command=cut)
    Editmenu.add_command(label="Copy",command=copy)
    Editmenu.add_command(label="Paste",command=paste)
    menubar.add_cascade(label="Edit",menu=Editmenu)
    #Edit  menu ends
    #Help menu starts 
    Helpmenu=Menu(menubar,tearoff=0)
    Helpmenu.add_command(label="About Notepad",command=about)
    menubar.add_cascade(label="Help",menu=Helpmenu)
    #Help menu ends
    top.config(menu=menubar)
    #adding scroll bar
    scroll=Scrollbar(textArea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set)
    top.mainloop()