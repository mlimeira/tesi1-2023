import datetime

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def iniciar():
    flg.start()
def pausar():
    flg.stop()
def add():
    flg.step(1)

janela = ttk.Window()
x = ttk.IntVar()

lbl = ttk.Label(janela, text='Exemplos do TTK Bootstrap', bootstyle=(INVERSE, PRIMARY))
lbl.pack()
cbt1 = ttk.Checkbutton(janela, variable=x, text='Default', bootstyle=SUCCESS)
cbt1.pack(side=LEFT, padx=10, pady=10)

cbt2 = ttk.Checkbutton(janela, text='Round', bootstyle=(ROUND, TOGGLE, DANGER))
cbt2.pack(side=LEFT, padx=10, pady=10)

cbt3 = ttk.Checkbutton(janela, text='Square', bootstyle=(SQUARE, TOGGLE))
cbt3.pack(side=LEFT, padx=10, pady=10)
dias = ['seg', 'ter', 'qua']

cbx = ttk.Combobox(janela, values=dias, state='readonly')
cbx.pack()

det = ttk.DateEntry(janela, dateformat='%d/%m/%Y', firstweekday=6, startdate=datetime.date(2019,11,23))
det.pack()

met = ttk.Meter(janela, interactive=True,
                subtext='Quilometragem',
                amountused=20,
                textright='Km',
                stripethickness=2,
                metertype='semi')
met.pack()

flg = ttk.Floodgauge(janela, mask='{}% de transferência', length=300)
flg.pack()

btn_start = ttk.Button(janela, text='Iniciar', command=iniciar, bootstyle=SUCCESS)
btn_start.pack(side=LEFT)
btn_pause = ttk.Button(janela, text='Pausar', command=pausar, bootstyle=DANGER)
btn_pause.pack(side=LEFT)
btn_add = ttk.Button(janela, text='Incrementar', command=add)
btn_add.pack(side=LEFT)


janela.mainloop()