import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
def iniciar():
    prb.start(10)
    for i in range(101):
        lbl['text'] = prb['value']

prb = ttk.Progressbar(janela,
                      orient=tk.HORIZONTAL,
                      mode='determinate')
prb.pack()

btn_start = ttk.Button(janela, text='Start',
                       command=iniciar)
btn_start.pack()
btn_stop = ttk.Button(janela, text='Stop',
                      command=prb.stop)
btn_stop.pack()
p = tk.IntVar()
p.set(0)
lbl = ttk.Label(janela, text=f'{p.get()}%')
lbl.pack()

janela.mainloop()