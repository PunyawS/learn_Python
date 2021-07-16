from tkinter import *

root = Tk()
root.title('Area Calculator')
root.geometry('300x200')

#Enter width 
Label(text='Enter width').grid(row=0)
width = IntVar()
et_width = Entry(width=30,textvariable=width,font=18)
et_width.grid(row=0,column=1)

#Enter height
Label(text='Enter height').grid(row=1)
height = IntVar()
et_height = Entry(width=30,textvariable=height,font=18)
et_height.grid(row=1,column=1)

#Show Answer
Label(text='Area of rectangle is : ').grid(row=2)
area1 = Entry(width=30, font=30)
area1.grid(row=2,column=1)

def calculate():
    width = et_width.get()
    height = et_height.get()
    area = int(width)*int(height)
    area1.insert(0,area)

def deletetext():
    width.delete(0,END)
    height.delete(0,END)
    area1.delete(0,END)

btn1=Button(text="calculate",command=calculate).grid(row=3,column=1,sticky=W)
btn1=Button(text="clear",command=deletetext).grid(row=3,column=1,sticky=E)
root.mainloop()