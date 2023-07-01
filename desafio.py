import operacoes

menu = """

    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair
    
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input('Informe o valor do Deposito: '))
        
        saldo, extrato = operacoes.depositar(valor, saldo, extrato)
    
    elif opcao == "s":
        valor = float(input('Informe o valor do saque: '))
        
        saldo, extrato, numero_saques = operacoes.sacar(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
    
    elif opcao == "e":
        operacoes.Consultar_Extrato(extrato, saldo)
    
    elif opcao == "q":
        break
    
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada')

