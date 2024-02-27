from tkinter import *
from tkinter import ttk

# Criando janela
janela = Tk()
janela.title('Exemplo de Combobox')

# Dias da semana

dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

# Criando o Combobox
combobox = ttk.Combobox(janela, values=dias_semana)
combobox.pack(padx=75, pady=20)

# Criando barra de prograsso

barra_progresso = ttk.Progressbar(janela, orient='horizontal', length=200, mode='determinate')
barra_progresso.pack()
barra_progresso.start(10)


janela.mainloop()