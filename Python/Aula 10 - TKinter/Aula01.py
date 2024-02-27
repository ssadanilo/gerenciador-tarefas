import tkinter as tk
from tkinter import (messagebox, )

def exibirMsg():
    messagebox.showinfo(title="Mostrar Produto", message=f"Produto:  {varNome.get()}   - R$   {varPreco.get()}   -  Qtd:  {varQuantidade.get()}")
    # messagebox.showerror(title="Mostrar Produto", message="Produto: " + varNome.get() + " - R$ " + varPreco.get() + " -  Qtd: " + varQuantidade.get())
    # messagebox.showwarning(title="Mostrar Produto", message="Produto: " + varNome.get() + " - R$ " + varPreco.get() + " -  Qtd: " + varQuantidade.get())

# Instanciando um objeto de Classe Tk
janela = tk.Tk() # Construtor
janela.geometry("600x600") # String: Largura x Altura da janela em Pixel
janela.title("Controle de Estoque - v.1.01") # Título

# Rótulo do Nome do Produto
lblNome = tk.Label(janela, text="Digite o Nome do PRODUTO: ", bg="black", fg="white")
lblNome.place(x=10 ,y=10)
# Caixa de Texto do Nome do Produto

varNome = tk.StringVar() # tk.IntVar tk.DoubleVar tk.BooleanVar (Outras variáveis)
txtNome = tk.Entry(janela, textvariable=varNome, width=50, font=("Tahoma", 14))
txtNome.place(x=180, y=10)

# Rótulo do Preço do Produto
lblPreço = tk.Label(janela, text="Digite o Preço do PRODUTO: ", bg="red", fg="white")
lblPreço.place(x=10 ,y=50)
# Caixa de Texto do Preço do Produto
varPreco = tk.StringVar()
txtPreço = tk.Entry(janela, textvariable=varPreco, width=5, font=("Tahoma", 14))
txtPreço.place(x=180, y=50)

# Rótulo do Quantidade do Produto
lblQuantidade = tk.Label(janela, text="Digite a Qto do PRODUTO: ", bg="blue", fg="white")
lblQuantidade.place(x=5 ,y=90)
# Caixa de Texto do Quantidade do Produto
varQuantidade = tk.StringVar()
txtQuantidade = tk.Entry(janela, textvariable=varQuantidade, width=5, font=("Tahoma", 14))
txtQuantidade.place(x=180, y=90)

#
frmBotao = tk.Frame(janela, relief=tk.RIDGE, borderwidth=1, bg="blue", width=500, height=5 )
frmBotao.place(x=32, y=300)

# Botão
btnExibir = tk.Button(janela, text="Exibir", command=exibirMsg )
btnExibir.place(x=10, y=130)

# CheckButton
almPerecivel = tk.Checkbutton(janela, text="Perecível")
almPerecivel.place(x=10, y=450)
almNaoPerecivel = tk.Checkbutton(janela, text="Não Perecível")
almNaoPerecivel.place(x=10, y=480)

# Radiobutton
rdNacional = tk.Radiobutton(janela, text="Nacional")
rdNacional.place(x=10, y=530)
rdImportado = tk.Radiobutton(janela, text="Nacional")
rdImportado.place(x=10, y=560)

janela.mainloop()