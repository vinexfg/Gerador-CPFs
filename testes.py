# from funcoes import Validador_cpf


# cpf_validador = Validador_cpf(70218140460)

# print(cpf_validador)








class Numero:
    def __init__(self, numero):
        self.numero = str(numero)

    def x(self):
        for digito in self.numero:
            print(digito)

valor =  12345678910
numeros = Numero(valor)
numeros.x()