from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from aluno import Aluno


class App:
    def __init__(self):
        self.alunos = []
        self.app = Tk()
        self.app.title('SysAlunos')

        # frame registro
        self.frame_registro = Frame(self.app)
        self.frame_registro.grid(row=0, column=1)

        # Label
        self.label_nome = Label(self.frame_registro, text="Nome:",
                                font="Tahoma 9 bold", fg="midnight blue")
        self.label_nome.grid(column=2, row=0)

        self.label_matricula = Label(self.frame_registro, text="Matricula:",
                                     font="Tahoma 9 bold", fg="midnight blue")
        self.label_matricula.grid(column=1, row=0)

        self.label_idade = Label(self.frame_registro, text="Idade:",
                                 font="Tahoma 9 bold", fg="midnight blue")
        self.label_idade.grid(column=3, row=0)

        self.label_cursos = Label(self.frame_registro, text="cursos:",
                                  font="Tahoma 9 bold", fg="midnight blue")
        self.label_cursos.grid(column=4, row=0)

        self.label_cursos = Label(self.frame_registro, text="Nota:",
                                  font="Tahoma 9 bold", fg="midnight blue")
        self.label_cursos.grid(column=5, row=0)

        # Combobox
        self.cursos = ['Python', 'Javascript', 'Java', 'Django', 'ReactJs']
        self.cb_cursos = ttk.Combobox(self.frame_registro, values=self.cursos, width=20, font='Tahoma 9')
        self.cb_cursos.grid(column=4, row=1, padx=5, pady=5)

        # Entry
        self.entry_nome = Entry(self.frame_registro, font="Tahoma 9")
        self.entry_nome.grid(column=2, row=1, padx=5, pady=5)

        self.entry_matricula = Entry(self.frame_registro, font="Tahoma 9", state=DISABLED)
        self.entry_matricula.grid(column=1, row=1, padx=5, pady=5)

        self.entry_idade = Entry(self.frame_registro, font="Tahoma 9")
        self.entry_idade.grid(column=3, row=1, padx=5, pady=5)

        self.entry_nota = Entry(self.frame_registro, font="Tahoma 9")
        self.entry_nota.grid(column=5, row=1, padx=5, pady=5)

        # botões

        self.button_adicionar = Button(self.frame_registro, font="Tahoma 9", width=7, text="Adicionar",
                                       command=self.adicionarAluno)
        self.button_adicionar.grid(row=0, pady=8, padx=8)

        self.button_editar = Button(self.frame_registro, font="Tahoma 9", width=7, text="Editar",
                                    command=self.editarAluno)
        self.button_editar.grid(row=1, pady=8, padx=8)

        self.button_excluir = Button(self.frame_registro, font="Tahoma 9", width=7, text="Excluir",
                                     command=self.excluirAluno)
        self.button_excluir.grid(row=2, pady=8, padx=8)

        # Frame(talvez não precise)

        self.frame = Frame(self.app)
        self.frame.grid(row=1, columnspan=1, pady=8, padx=8, column=1)

        # TreeView
        self.colunas = ['Matricula', 'Nome', 'Idade', 'Curso', 'Nota']
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas, show='headings')
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
        self.tabela.pack()
        self.tabela.bind('<ButtonRelease-1>', self.selecionarAluno)

        self.app.mainloop()

    def adicionarAluno(self) -> None:
        nome = self.entry_nome.get()
        idade = int(self.entry_idade.get())
        curso = self.cb_cursos.get()
        nota = float(self.entry_nota.get())
        aluno = Aluno(nome, idade, curso, nota)
        self.alunos.append(aluno)
        self.atualizaTabela()
        messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso")
        self.limparCampos()

    def limparCampos(self) -> None:
        self.entry_nome.delete(0, END)
        self.entry_nota.delete(0, END)
        self.entry_idade.delete(0, END)
        self.cb_cursos.set("")
        self.entry_matricula.config(state=NORMAL)
        self.entry_matricula.delete(0, END)
        self.entry_matricula.config(state=DISABLED)

    def atualizaTabela(self):
        # Limpa a tabela
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        # preencher a tabela
        for aluno in self.alunos:
            self.tabela.insert("", END, values=(aluno.matricula,
                                                aluno.nome,
                                                aluno.idade,
                                                aluno.curso,
                                                aluno.nota))

    def selecionarAluno(self, event):
        linha_selecionada = self.tabela.selection()[0]
        item = self.tabela.item(linha_selecionada)['values']
        self.limparCampos()
        self.entry_matricula.config(state=NORMAL)
        self.entry_matricula.insert(0, item[0])
        self.entry_matricula.config(state=DISABLED)
        self.entry_nome.insert(0, item[1])
        self.entry_idade.insert(0, str(item[2]))
        self.cb_cursos.set(item[3])
        self.entry_nota.insert(0, str(item[4]))

    def editarAluno(self):
        matricula = self.entry_matricula.get()

        for aluno in self.alunos:
            if aluno.matricula == matricula:
                aluno.nome = self.entry_nome.get()
                aluno.idade = int(self.entry_idade.get())
                aluno.curso = self.cb_cursos.get()
                aluno.nota = float(self.entry_nota.get())
                messagebox.showinfo("Sucesso", "Dados atualizados")


        self.limparCampos()
        self.atualizaTabela()
        print(self.alunos)

    def excluirAluno(self):
        pass


if __name__ == "__main__":
    app = App()
