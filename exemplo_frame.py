import tkinter as tk

janela = tk.Tk()

frame1 = tk.Frame(janela, bg='green', width=200)
frame1.pack(side=tk.TOP, expand=True, fill=tk.X)
btn1 = tk.Button(frame1, text='1')
btn1.pack()
btn2 = tk.Button(frame1, text='2')
btn2.pack()
btn3 = tk.Button(frame1, text='3')
btn3.pack()

frame2 = tk.LabelFrame(janela,
                       text='Título do Frame',
                       labelanchor=tk.NW,
                       height=200, width=200)
frame2.pack()
btn4 = tk.Button(frame2, text='Botão 4')
btn4.grid(row=0, column=0)
btn5 = tk.Button(frame2, text='Botão 5')
btn5.grid(row=0, column=1)
btn6 = tk.Button(frame2, text='Botão 6')
btn6.grid(row=1, column=0, columnspan=2)

janela.mainloop()