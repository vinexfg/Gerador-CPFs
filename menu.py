from funcoes import Pessoa, Validador_cpf


print('Bem vindo ao gerador e validador de CPF ')
print('_____________________________________________')
print('Escolha uma das opçõe ')
while True:
    try:
        opcao = int(input('[1]validar [2]gerar [3]sair '))
        if opcao == 1:
            
