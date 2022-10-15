# from os import name
# import tkinter as tk
# root=tk.Tk()
# root.geometry("600x400")
# name_var=tk.StringVar()
# passw_var=tk.StringVar()

# def submit():
#     name=name_var.get()
#     password=passw_var.get()
#     lable_name=tk.Label(text=name)
#     lable_name.place (x=100,y=120)

#     lable_passwd = tk.Label(text=password)
#     lable_passwd.place(x=120,y=150)

    # print("The name is : " + name)
    # print("The password is : " + password)
#     name_var.set("")
#     passw_var.set("")
	
# name_label = tk.Label(root, text = 'Username', font=("Arial",10, 'bold'))
# name_entry = tk.Entry(root,textvariable = name_var, font=("Arial",10,'normal'))
# passw_label = tk.Label(root, text = 'Password', font = ("Arial",10,'bold'))
# passw_entry=tk.Entry(root, textvariable = passw_var, font = ("Arial",10,'normal'), show = '*')
# sub_btn=tk.Button(root,text = 'Submit', command = submit)


# name_label.grid(row=0,column=0)
# name_entry.grid(row=0,column=1)
# passw_label.grid(row=1,column=0)
# passw_entry.grid(row=1,column=1)
# sub_btn.grid(row=2,column=1)

# root.mainloop()

# .........................................................

# from cProfile import label
# from cgitb import text

# from operator import imod
# from tkinter import *
# import tkinter as tk
# from turtle import width

# root =Tk()
# root.geometry("300x200")

# W = Label(root, text = 'Gujarat University',font = "50").pack()
# Checkbutton1 = tk.IntVar()
# Checkbutton2 = tk.IntVar()
# Checkbutton3 = tk.IntVar()



# Button1 = Checkbutton(root,text = "Tutorial",variable = Checkbutton1,
# onvalue = 1,offvalue  = 0,height = 2,width = 10 )

# Button2 = Checkbutton(root,text = "Tutorial",variable = Checkbutton2,
# onvalue = 1,offvalue  = 0,height = 2,width = 10 )

# Button3 = Checkbutton(root,text = "Tutorial",variable = Checkbutton3,
# onvalue = 1,offvalue  = 0,height = 2,width = 10 )

# Button1.pack()
# Button2.pack()
# Button3.pack()

# root.mainloop()



from operator import imod
from tkinter import*
import tkinter as tk

root=Tk()

root.geometry("500x500")
listsample=Listbox(root,width=70,height=30,fg="white",bg="black",font=('Arial 30'))
listsample.insert(1,"Software Develoment")
listsample.insert(2,"Animation")
listsample.insert(3,"It")

listsample.pack()

root.mainloop()

import tkinter as tk
from tkinter import*

root = Tk()
root.geometry("500x500")
# declaring Label



root.mainloop()





