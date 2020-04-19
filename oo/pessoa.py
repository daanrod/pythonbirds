class Pessoa:
    # atributo de classe default
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimenta_da_class = super().cumprimentar()
        return f'{cumprimenta_da_class}. Aperto de mão.'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    diego = Mutante(nome='Diego')
    danilo = Homem(diego, nome='Danilo')
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
    print(Pessoa.metodo_estatico(), danilo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), danilo.nome_e_atributos_de_classe())

    print(diego.cumprimentar())
    print(danilo.cumprimentar())