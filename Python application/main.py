
from tkinter import *

import tkinter.messagebox
third_party_root = Tk()

# gui logic
third_party_root.geometry("844x434")


# minimum size of application
third_party_root.minsize(800,100)

# title of the application
third_party_root.title("Third Party Calculator")
# lable

text = Label(text="Third Party Premium Calculator ",background="green",font = ("bold",25, "bold"),borderwidth=5,padx=10,pady=20)
text.pack(side="top",fill=X)
#text2 = Label(text="This project has been created for the purpose of learning. The calculation used in the project "
  #                 "is based on tarrif rate given by beema pradhikaran",highlightcolor="red")
#text2.pack(anchor="nw",fill=X)

def refresh():
    tkinter.messagebox.showinfo(title="Alert",message="Values are cleared")
def tp():
    if ccvalue.get()<150 :
        x=1000
    elif ccvalue.get() >=150 and ccvalue.get() < 250:
        x=1200
    else:
        x=1400

    premium = round((x+10+nvalue.get()*250)*1.13,1)
    tkinter.messagebox.showinfo(title="Result",message=premium)

#tkinter.messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message")
# creating frame
f1=Frame(third_party_root,borderwidth=6)
f1.pack(side=LEFT,anchor="nw")
#b1=Button(f1,fg="black",text="Re-Fresh",command=refresh)
#b1.pack()



year= Label(f1,text="Year of Manufacture:")
cc =Label(f1,text="CC of Vehilce:")
n=Label(f1,text="Number of Seat:")
year.grid()
cc.grid(row=1)
n.grid(row=2)
yearvalue = IntVar()
ccvalue=IntVar()
nvalue=IntVar()
yearentry= Entry(f1,textvariable=yearvalue)
ccentry=Entry(f1,textvariable=ccvalue)
nenter=Entry(f1,textvariable=nvalue)
yearentry.grid(row=0,column=1)
ccentry.grid(row=1,column=1)
nenter.grid(row=2,column=1)

Button(f1,text="Calculate",command=tp).grid()





third_party_root.mainloop()

