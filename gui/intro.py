from tkinter import *

top = Tk()

redbtn = Button(top, text='red', fg='red')

redbtn.pack(side='left')

bluebtn = Button(top,text='blue', fg='blue')
bluebtn.pack(side='right')

top.mainloop()