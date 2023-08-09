import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

janela = ttk.Window(themename='litera')

stx = ScrolledText(janela, height=5, width=30, autohide=True, bootstyle=(DARK, ROUND))
stx.pack(fill=BOTH, expand=YES)
stx.insert(END, 'Deixe seu comentário aqui.')

janela.mainloop()