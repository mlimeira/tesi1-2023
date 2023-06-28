import threading
import time
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
pause = False
def iniciar():
    #prb.start(10)
    valor = p.get()
    btn_start.config(state=tk.DISABLED)
    btn_pause.config(state='active')
    btn_stop.config(state='active')
    for i in range(valor, 101):
        if pause:
            break
        p.set(i)
        lbl['text'] = f"{prb['value']}%"
        time.sleep(0.1)

def thread():
    global pause
    pause = False
    th = threading.Thread(target=iniciar)
    th.start()

def pausar():
    global pause
    pause = True
    btn_start.config(state='active', text='Restart')

def parar():
    p.set(0)
    lbl.config(text='0%')
    pausar()
    btn_start.config(text='Start')
    btn_pause.config(state='disabled')
    btn_stop.config(state='disabled')

p = tk.IntVar()
p.set(0)
prb = ttk.Progressbar(janela, variable=p,
                      orient=tk.HORIZONTAL,
                      mode='determinate')
prb.pack()

btn_start = ttk.Button(janela, text='Start',
                       command=thread)
btn_start.pack()
btn_pause = ttk.Button(janela, text='Pause', state='disabled',
                      command=pausar)
btn_pause.pack()
btn_stop = ttk.Button(janela, text='Stop', state='disabled',
                      command=parar)
btn_stop.pack()

lbl = ttk.Label(janela, text=f'{p.get()}%')
lbl.pack()

janela.mainloop()