
def validador(cpf):
    cpf_digitado = int(input('CPF: '))
    nove_digitos = cpf_digitado[:9]
    contador_regressivo = 10
    resultado = 0
    for digito in cpf_digitado:
        resultado += int(digito) * contador_regressivo
        contador_regressivo -= 1
    digito = digito if digito <= 9 else 0
