


class Pessoa:

    def __init__(self,nome,sobrenome,idade,entrada= True) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.entrada = entrada

    def verificacao(self, entrada ):
        if self.idade < 18:
            print(f'Senhor {self.nome}, infelizmente somente maiores de idade pode usar o programa')
            self.entrada = False
            return self.entrada
        
    def entrada_sistema(self):
        if self.verificacao():
            print(f'{self.nome} {self.sobrenome} entrou no sistema..')
        else:
            print(f'{self.nome} {self.sobrenome} não pode entrar no sistema..')
    

class Validador_cpf:
    def __init__(self, cpf):
        self.cpf = cpf
    

    def validador(self):
        qtd_digitos_permitido = 11
        if self.cpf > qtd_digitos_permitido:
            print('Infelizmente o cpf foi digitado incorreto, reinicie o programa...')
        else:
            while True:
                self.cpf[:9]
                for digito in self.cpf:
                    print(digito)
            

