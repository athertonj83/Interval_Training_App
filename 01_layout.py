# Starting out with a layout for the app
import tkinter as tk
from tkinter import *

class trainingApp(tk.Frame):
    def __init__(self, master):
        super(trainingApp, self).__init__(master)
        self.width = 710
        self.height = 610
        self.canvas = tk.Canvas(self, bg='#aaaaff', width=self.width, height=self.height)
        self.canvas.pack()
        self.pack()

        #Adding a button
        # redbutton = Button(self.canvas, text="Test", fg="red")
        # redbutton.pack()
        # redbutton.place(relheight=0.5, relwidth=0.5)

        labelWarmUp=Label(self.canvas, text="Warm Up")
        #labelWarmUp.pack()
        labelWarmUp.place(relx=0.3, rely=0.12, anchor='n')
        #labelWarmUp.grid(row=0,column=0)

        labelCoolDown=Label(self.canvas, text="Cool Down")
        #labelCoolDown.pack()
        labelCoolDown.place(relx=0.3, rely=0.12, anchor='e')
        #labelCoolDown.grid(row=1,column=0)


        # entryWarmUp=Entry(self.canvas,bd=5)
        # entryWarmUp.pack(side = RIGHT)
        # labelWarmUp.place(relheight=0.12, relwidth=0.3)

#         MyButton1 = Button(master, text="BUTTON1", width=10, command=callback)
# MyButton1.grid(row=0, column=0)
#
# MyButton2 = Button(master, text="BUTTON2", width=10, command=callback)
# MyButton2.grid(row=1, column=0)
#
# MyButton3 = Button(master, text="BUTTON3", width=10, command=callback)
# MyButton3.grid(row=2, column=0)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Jen's Training App!")
    jen = trainingApp(root)
    jen.mainloop()
