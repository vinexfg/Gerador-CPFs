
print('Prencha os dados: ')
def dados_cliente(nome, idade, Email):
        print(f'Seja bem vindo cliente {nome}')
        print(f'Vejo que voce tem {idade} e podera acessar nosso site.')
        print(f'{nome}, {idade}, {Email}')
    
def validador(cpf):
        cpf = cpf[:9]
        contador_regressivo = 10
        resultado = 0
        for digito in cpf:
                resultado += (digito * contador_regressivo)
                contador_regressivo -= 10
            digito = (resultado * 10) % 11
            resultado
        
                
                
        