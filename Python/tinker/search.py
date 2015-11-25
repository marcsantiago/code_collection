__author__ = 'marcsantago'
import tkinter

def action():
    print('clicked')

tk = tkinter.Tk()
search = tkinter.Button(tk, text='search', command=action)
search.pack()
tkinter.mainloop()