from funcoes import Pessoa, Validador_cpf, GeradorCPF


print('Bem vindo ao gerador e validador de CPF ')
print('_____________________________________________')
print('Escolha uma das opçõe ')
while True:
    try:
        opcao = int(input('[1]validar [2]gerar [3]sair '))
        if opcao == 1:
            cpf_input = input('Digite o CPF (apenas numeros): ')
            validador = Validador_cpf(cpf_input)
            validador.validar()
        elif opcao == 2:
            cpf_gerado = GeradorCPF.gerar()
            print(f'CPF gerado: {cpf_gerado}')

        elif opcao == 3:
            print('saindo...')
            break
        else:
            print('Opção invalida, tente novamente.')
    except ValueError:
        print('Entrada  invalida, por favor insira um numero')

    