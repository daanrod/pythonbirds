class Pessoa:
    # atributo de classe default
    olhos = 2

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
    # atributos podem ser criados dinamicamente, mas é recomendados apenas para
    # eventialidades
    danilo.sobrenome = "Barros"
    # atributos podem ser deletados dinamicamente
    del danilo.filhos
    danilo.olhos = 1
    del danilo.olhos
    print(diego.__dict__)
    print(danilo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(diego.olhos)
    print(danilo.olhos)
    print(id(Pessoa.olhos), id(danilo.olhos), id(diego.olhos))

