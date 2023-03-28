from conta_corrente import *
from conta_poupanca import *
from sys import exit
from random import randint

caracter_proibido = "!?:;<>,/´`~^\|'\"@#$%&*()[]{}.+-_§"
print("-"*35)
print(f"{'CRIANDO CADASTRO':^35}")
print("-"*35)

while True:
    nome = input("Digite seu nome: ")
    for c in nome:
        if c in caracter_proibido:
            print("Um ou mais caracteres em seu nome não são permitidos.\n")
            erro = True
            sleep(0.5)
            break
        else:
            erro = False
    if not erro:
        break
    
cliente_corrente = ContaCorrente(id=str(randint(100, 999)), saldo=0.00, limite=5000)
cliente_poupanca = ContaPoupanca(id=str(randint(1000, 9999)), saldo=0.00)

sleep(1)
print("Assegurando informações...")
sleep(1)
print("Criando Contas...")
sleep(1.5)
print("-"*35)
print()

while True:
    print("-"*45)
    print(f"{'INICIO':^45}")
    print("-"*45)
    print(f"Olá {nome}! Seja bem-vindo(a) ao App Banco Ultra.\n"
           "O que você deseja fazer hoje?")
    while True:
            try:
                acesso = int(input("\n1- Acessar Conta Corrente"
                                   "\n2- Acessar Conta Poupança"
                                   "\n3- Encerrar sessão"
                                   "\nSelecione: "))
                break
            except (ValueError, KeyboardInterrupt):
                print("Valor inválido. Selecione uma das operações listadas.\n")
                sleep(1)
    print("-"*45)

    if acesso == 1:
        print("-"*45)
        print(f"{'CONTA CORRENTE':^45}")
        print("-"*45)
        while True:
            print(f"ID da conta: {cliente_corrente.id}\n"
                  f"Saldo: R${cliente_corrente.saldo:.2f}\n"
                  f"Limite disponível: R${cliente_corrente.limite:.2f}")   
            while True:
                try:
                    acesso = int(input("\n1- Depositar"
                                       "\n2- Sacar"
                                       "\n3- Empréstimo"
                                       "\n4- Transferência Interna"
                                       "\n5- Voltar"
                                       "\nSelecione uma das operações acima: "))
                    break
                except (ValueError, KeyboardInterrupt):
                    print("Valor inválido. Selecione uma das operações listadas.\n")
                    sleep(1)
                
            if acesso == 1:
                cliente_corrente.depositar()
            elif acesso == 2:
                cliente_corrente.sacar()
            elif acesso == 3:
                cliente_corrente.emprestimo()
            elif acesso == 4:
                cliente_corrente.tranferir_para_poupanca(cliente_poupanca)
            elif acesso == 5:
                break
            else:
                print("Opção não encontrada.\n")
                sleep(1)
                
        print("-"*45)
        sleep(1.5)
    
    elif acesso == 2:
        print("-"*45)
        print(f"{'CONTA POUPANÇA':^45}")
        print("-"*45)
        while True:
            print(f"ID da conta: {cliente_poupanca.id}\n"
                  f"Saldo: R${cliente_poupanca.saldo:.2f}")    
            while True:
                try:
                    acesso = int(input("\n1- Depositar"
                                       "\n2- Sacar"
                                       "\n3- Verificar Rendimentos"
                                       "\n4- Tranferência Interna"
                                       "\n5- Voltar"
                                       "\nSelecione uma das operações acima: "))
                    break
                except (ValueError, KeyboardInterrupt):
                    print("Valor inválido. Selecione uma das operações listadas.\n")
                    sleep(1)
                
            if acesso == 1:
                cliente_poupanca.depositar()
            elif acesso == 2:
                cliente_poupanca.sacar()
            elif acesso == 3:
                cliente_poupanca.verificar_rendimento()
            elif acesso == 4:
                cliente_poupanca.tranferir_para_corrente(cliente_corrente)
            elif acesso == 5:
                break
            else:
                print("Opção não encontrada.\n")
                sleep(1)
                
        print("-"*45)
        sleep(1.5)

    elif acesso == 3:
        while True:    
            sleep(1)
            while True:
                try:
                    acesso = int(input("\nDeseja mesmo encerrar a sessão?:"
                                       "\n1- Sim"
                                       "\n2- Não"
                                       "\nSelecione: "))
                    break
                except (ValueError, KeyboardInterrupt):
                    print("Valor inválido. Selecione uma das operações listadas.\n")
                    sleep(1)
            
            if acesso == 1:
                print("Esperamos vê-lo novamente em breve!")
                print("-"*45)
                sleep(2)
                exit()
            elif acesso == 2:
                print("Retornando...")
                sleep(1.5)
                break
            else:
                print("Opção não encontrada.\n")
                sleep(1)
            
    else:
        print("Opção não encontrada.\n")
        sleep(1)