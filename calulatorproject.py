from tkinter import*

def amalgar(labl,txt):
    g = labl['text']
    labl.config(text=g+txt)
    labl.update()

def hesab(labl):
    g = labl['text']    
    # g = g.repalce("×","*")
    # g = g.replace("÷","/")
    gavab = eval(g)
    labl.config(text=str(gavab))
    labl.update()
    
def clear(labl):
    labl.config(text="")
    
root = Tk()
root.title("calculator")
root.geometry("320x345")
root.config(bg="black")

entry = Label(root,text="",width=45,height=3,)
entry.grid(row=0,column=0,columnspan=4,sticky="nsew")


but_1 = Button(root,text="1",width=10,height=3,fg="white",bg="#2a2d42",bd=1,command=lambda:amalgar(entry,"1"))
but_2 = Button(root,text="2",width=10,height=3,fg="white",bg="#2a2d42",bd=1,command=lambda:amalgar(entry,"2"))
but_3 = Button(root,text="3",width=10,height=3,fg="white",bg="#2a2d42",bd=1,command=lambda:amalgar(entry,"3"))
but_4 = Button(root,text="4",width=10,height=3,fg="white",bg="#2a2d42",bd=1,command=lambda:amalgar(entry,"4"))
but_5 = Button(root,text="5",width=10,height=3,fg="white",bg="#2a2d42",bd=1,command=lambda:amalgar(entry,"5"))
but_6 = Button(root,text="6",width=10,height=3,fg="white",bg="#2a2d42",bd=1,command=lambda:amalgar(entry,"6"))
but_7 = Button(root,text="7",width=10,height=3,fg="white",bg="#2a2d42",bd=1,command=lambda:amalgar(entry,"7"))
but_8 = Button(root,text="8",width=10,height=3,fg="white",bg="#2a2d42",bd=1,command=lambda:amalgar(entry,"8"))
but_9 = Button(root,text="9",width=10,height=3,fg="white",bg="#2a2d42",bd=1,command=lambda:amalgar(entry,"9"))
but_0 = Button(root,text="0",padx=72,height=3,fg="white",bg="#2a2d42",bd=1,command=lambda:amalgar(entry,"0"))

but_clear = Button(root,text="C",bd=1,padx=30,pady=15,bg="#2f9037",command=lambda:clear(entry))
but_add = Button(root,text="+",width=10,height=3,fg="white",bg="#0d1d2d",bd=1,command=lambda:amalgar(entry,"+"))
but_minus = Button(root,text="-",width=10,height=3,fg="white",bg="#0d1d2d",bd=1,command=lambda:amalgar(entry,"-"))
but_divide = Button(root,text="÷",width=10,height=3,fg="white",bg="#0d1d2d",bd=1,command=lambda:amalgar(entry,"/"))
but_modu = Button(root,text="%",width=10,height=3,fg="white",bg="#0d1d2d",bd=1,command=lambda:amalgar(entry,"%"))
but_multi = Button(root,text="×",width=10,height=3,fg="white",bg="#0d1d2d",bd=1,command=lambda:amalgar(entry,"*"))
but_dot = Button(root,text=".",width=10,height=3,fg="white",bg="#0d1d2d",bd=1,command=lambda:amalgar(entry,"."))
but_equal = Button(root,text="=",width=10,pady=45,fg="black",bg="#2f9037",bd=1,command=lambda:hesab(entry))

but_1.grid(row=2,column=0,pady=2)
but_2.grid(row=2,column=1,pady=2)
but_3.grid(row=2,column=2,pady=2)
but_4.grid(row=3,column=0,pady=2)
but_5.grid(row=3,column=1,pady=2)
but_6.grid(row=3,column=2,pady=2)
but_add.grid(row=3,column=3,pady=2)
but_7.grid(row=4,column=0,pady=2)
but_8.grid(row=4,column=1,pady=2)
but_9.grid(row=4,column=2,pady=2)
but_0.grid(row=5,column=0,columnspan=2,pady=2)

but_dot.grid(row=5,column=2,pady=2)
but_minus.grid(row=2,column=3,pady=2)
but_equal.grid(row=4,column=3,rowspan=2,pady=2)
but_multi.grid(row=1,column=0,padx=1,pady=2)
but_modu.grid(row=1,column=1,padx=1,pady=2)
but_divide.grid(row=1,column=2,padx=1,pady=2)
but_clear.grid(row=1,column=3,padx=2,pady=2)
root.mainloop()