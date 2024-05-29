import random

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    @property
    def verificacao(self):
        if self.idade < 18:
            print(f'Senhor(a) {self.nome}, infelizmente somente maiores de idade podem usar o programa')
            return False
        return True

    def entrada_sistema(self):
        if self.verificacao:
            print(f'{self.nome} {self.sobrenome} entrou no sistema.')
        else:
            print(f'{self.nome} {self.sobrenome} não pode entrar no sistema.')

class ValidadorCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def primeiro_digito(self):
        soma = sum(int(digito) * peso for digito, peso in zip(self.cpf[:9], range(10, 1, -1)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    def segundo_digito(self):
        soma = sum(int(digito) * peso for digito, peso in zip(self.cpf[:10], range(11, 1, -1)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    def validar(self):
        if len(self.cpf) != 11 or not self.cpf.isdigit():
            print('CPF inválido. Deve conter 11 dígitos numéricos.')
            return False
        if int(self.cpf[-2]) == self.primeiro_digito() and int(self.cpf[-1]) == self.segundo_digito():
            print('CPF válido.')
            return True
        print('CPF inválido.')
        return False

class GeradorCPF:
    @staticmethod
    def gerar():
        nove_digitos = [random.randint(0, 9) for _ in range(9)]
        cpf_parcial = ''.join(map(str, nove_digitos))

        validador = ValidadorCPF(cpf_parcial + '00')
        digito1 = validador.primeiro_digito()
        cpf_com_digito1 = cpf_parcial + str(digito1)
        
        validador = ValidadorCPF(cpf_com_digito1 + '0')
        digito2 = validador.segundo_digito()

        cpf_final = cpf_com_digito1 + str(digito2)
        return cpf_final

