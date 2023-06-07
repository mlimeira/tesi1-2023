import tkinter as tk

janela = tk.Tk()
janela.geometry('300x300')

lbl1 = tk.Label(janela, text='X=0,Y=0', bg='blue')
lbl1.place(x=0, y=0, anchor=tk.NW)
lbl2 = tk.Label(janela, text='X=100,Y=25', bg='red')
lbl2.place(relx=.5, rely=.5, anchor=tk.CENTER)
lbl3 = tk.Label(janela, text='X=200,Y=50', fg='black', bg='yellow')
lbl3.place(x=200, y=50)



janela.mainloop()