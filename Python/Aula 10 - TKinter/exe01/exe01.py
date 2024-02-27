import tkinter as tk

def cadastro_alunos():
    nome = entry_nome.get()
    idade = entry_idade.get()
    nota = entry_nota.get()
    print('Nome:', nome, 'Idade:', idade, 'Nota:', nota)

# Criando janela
root = tk.Tk()
root.title('Cadastro de alunos')

# Criando interface
label_nome = tk.Label(root, text='Nome:', font=('Tahoma', 10, 'bold'))
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_idade = tk.Label(root, text='Idade:', font=('Tahoma', 10, 'bold'))
label_idade.grid(row=1, column=0, padx=5, pady=5)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1, padx=5, pady=5)

label_nota = tk.Label(root, text='Nota:', font=('Tahoma', 10, 'bold'))
label_nota.grid(row=2, column=0, padx=5, pady=5)
entry_nota = tk.Entry(root)
entry_nota.grid(row=2, column=1, padx=5, pady=5)

button_cadastro = tk.Button(root, text='Cadastrar', command=cadastro_alunos)
button_cadastro.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()

