import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title('Botão de rádio')

# Responsividade na janela
porcentual:float = 80/100
geometria:str = f'{int(janela.winfo_screenwidth()*porcentual)}x{int(janela.winfo_screenwidth()*porcentual)}'
janela.geometry(geometria)
janela.resizable(False, False)

label1 = tk.Label(janela, text='Rótulo Antigo')
label2 = ttk.Label(janela, text='Rótulo Novo')
label1.pack()
label2.pack()

caixa1 = tk.Entry().pack()

janela.mainloop()