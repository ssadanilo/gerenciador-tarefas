# Importando Tkinter
import tkinter as tk
from tkinter import messagebox

# Criando cor
cor_branca = '#f5f9fa'
cor_amarela = '#f2eb1d'

# Criando a função
def converter_medida():
    valor_correto = entry_centimetro.get()
    if valor_correto.replace(',','').replace('.','').isdigit(): # Verifica se é um número que foi digitado
        cm = float(valor_correto.replace(',', '.')) # Corrige a vírgula pelo ponto
        metro = cm / 100
        label_resposta.config(text=f'{cm} centimetros equivalem a {metro:.2f} metros') 
    else:
        messagebox.showerror('Erro!', 'Insira um número válido') # Cria uma mensagem de erro
    
# Criando janela
janela = tk.Tk()
janela.title('Conversor de Medidas')
janela.geometry('700x100')
janela.config(bg=cor_branca)

# Criando widgates
label_explicacao = tk.Label(janela, text='Digite o valor em centímetro no espaço correspondente a ele para converter em metro', bg= cor_amarela, font=('tahoma',12))
label_explicacao.place(x=5, y=0)

label_centimetro = tk.Label(janela, text='Centímetro', font=('tahoma',10))
label_centimetro.place(x=5, y=30)
entry_centimetro = tk.Entry(janela,)
entry_centimetro.place(x=80, y=30)

label_resposta = tk.Label(janela, text='', bg= cor_amarela, font=('tahoma',12))
label_resposta.place(x=80, y=60)

# Criando botão
botao_calcular = tk.Button(janela, text='Calcular', font=('tahoma',10), command=converter_medida)
botao_calcular.place(x=5, y=60)

# Criando loop
janela.mainloop()