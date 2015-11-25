__author__ = 'marcsantago'
import tkinter
tk = tkinter.Tk()
tk.title('test')
canvas = tkinter.Canvas(tk)
canvas.pack()
canvas.create_rectangle(20, 10, 120, 90, fill='blue')
canvas.create_rectangle(100, 10, 220, 90, fill='black')

tkinter.mainloop()