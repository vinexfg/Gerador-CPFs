


class Pessoa:

    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.entrada = None
        self.verificacao
        
    def verificacao(self):
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
    

    def primeiro_digito(self):
        self.cpf
        for digito in range(self.cpf):
            print(digito)

    def validador(self):
        qtd_digitos_permitido = 11
        if self.cpf > qtd_digitos_permitido:
            print('...')
        else:
            pass
            

