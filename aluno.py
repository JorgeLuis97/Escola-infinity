import uuid


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # Gera um identificado unico
        self.matricula = uuid.uuid1()


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, nota):
        super().__init__(nome, idade)
        self.curso = curso
        self.nota = nota

    def __repr__(self):
        return f'Matricula: {self.matricula} \n' \
               f'Nome: {self.nome} \n' \
               f'Idade: {self.idade} \n' \
               f'Curso: {self.curso} \n' \
               f'Nota: {self.nota}'

if __name__ == '__main__':
    aluno = Aluno('Jonas',15,'Nada', 2.5)
    print(aluno)