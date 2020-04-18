class Pessoa:
    def __init__(self, *filhos, nome=None, idade=27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    diego = Pessoa(nome='Diego')
    danilo = Pessoa(diego, nome='Danilo')
    print(Pessoa.cumprimentar(danilo))
    print(id(danilo))
    print((danilo.cumprimentar()))
    print(danilo.nome)
    print(danilo.idade)
    for filho in danilo.filhos:
        print(filho.nome)
