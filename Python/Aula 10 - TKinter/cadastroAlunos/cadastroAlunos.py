import tkinter as tk

def cadastrar_aluno():
    nome = entry_nome.get()
    idade = entry_idade.get()
    nota = entry_nota.get()
    
    print("Aluno cadastrado:")
    print("Nome:", nome)
    print("Idade:", idade)
    print("Nota:", nota)
    print("------------------")

# Configurações da janela principal
root = tk.Tk()
root.title("Cadastro de Alunos")

# Componentes da interface
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_idade = tk.Label(root, text="Idade:")
label_idade.grid(row=1, column=0, padx=5, pady=5)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1, padx=5, pady=5)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=2, column=0, padx=5, pady=5)
entry_nota = tk.Entry(root)
entry_nota.grid(row=2, column=1, padx=5, pady=5)

button_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_aluno)
button_cadastrar.grid(row=3, columnspan=2, padx=5, pady=5)

# Iniciar o loop principal da aplicação
root.mainloop()
