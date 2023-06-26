import tkinter as tk

janela = tk.Tk()
frame = tk.Frame(janela)
frame.pack()
#piramide
btn1 = tk.Button(frame, text='1')
btn1.grid(row=0, column=1)
btn2 = tk.Button(frame, text='2')
btn2.grid(row=1, column=0, columnspan=2)
btn3 = tk.Button(frame, text='3')
btn3.grid(row=1, column=1, columnspan=2)
btn4 = tk.Button(frame, text='4')
btn4.grid(row=2, column=0)
btn5 = tk.Button(frame, text='5')
btn5.grid(row=2, column=1)
btn6 = tk.Button(frame, text='6')
btn6.grid(row=2, column=2)

janela.mainloop()