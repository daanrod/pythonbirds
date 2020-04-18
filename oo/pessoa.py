class Pessoa:
    def __init__(self, nome=None, idade=27):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Diego')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print((p.cumprimentar()))
    print(p.nome)
    p.nome = 'Danilo'
    print(p.nome)
    print(p.idade)
