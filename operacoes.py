# Função para efetuar o deposito em conta
def depositar(valor: float, saldo: float, extrato: str) -> None:
    
    if valor > 0:
        saldo += valor
        extrato += f'Depósito R${valor:.2f}\n'
    
    else:
        print("Operacao falho! O valor informar é inválido!")
    
    return saldo, extrato

# Função para efetuar saque em conta
def sacar(valor: float, saldo: float, extrato: str, limite: float, numero_saques: int, LIMITE_SAQUES: int) -> None:
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente!")
    
    elif excedeu_limite:
        print('Operação falhou! O valor de saque excede o limite.')
    
    elif excedeu_saques:
        print('Operação falhou! Número máximo de saques excedido!')
    
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'
        numero_saques += 1
    
    else:
        print('Operação falhou! O valor informado é invalido')
    
    return saldo, extrato, numero_saques

# Função para ver o Extrato da conta
def Consultar_Extrato(extrato: str, saldo: float) -> None:
    print('\n==========EXTRATO==========')
    print('Não foram realizada movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R${saldo:.2f}')
    print("===========================")