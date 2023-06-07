import tkinter as tk

janela = tk.Tk()

lbl1 = tk.Label(janela, text='LEFT1', bg='magenta')
lbl1.pack(padx=20, ipadx=10, fill=tk.Y, side=tk.LEFT)

lbl2 = tk.Label(janela, text='RIGHT1', bg='red')
lbl2.pack(padx=20, ipadx=10,
          fill=tk.BOTH, expand=True, side=tk.RIGHT)

lbl3 = tk.Label(janela, text='LEFT2', bg='blue')
lbl3.pack(padx=20, ipadx=10,
          fill=tk.X, expand=True, side=tk.LEFT)

lbl4 = tk.Label(janela, text='RIGHT2', bg='black')
lbl4.pack(padx=20, ipadx=10, side=tk.RIGHT)

janela.mainloop()