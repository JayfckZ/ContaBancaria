from conta import *
from time import sleep

class ContaCorrente(Conta):
    def __init__(self, id, saldo, limite, tem_emprestimo=False, valor_emprestimo=0, parcelas=0):
        super().__init__(id, saldo)
        self.limite = limite
        self.tem_emprestimo = tem_emprestimo
        self.valor_emprestimo = valor_emprestimo
        self.parcelas = parcelas

    def depositar(self):
        print("-"*45)
        while True:
            try:
                valor = float(input("Informe o valor a depositar: "))
                break
            except (ValueError, KeyboardInterrupt):
                print("Valor inválido. Caso queira adicionar casa decimais utilize pontos (\".\") para separar as casas.\n"
                      "Se não, utilize apenas números.\n")
                sleep(1)


        if valor < 0:
            print(f"Valores negativos não são permitidos. Alternando para R${valor * -1}.")
            valor = valor * -1
        
        sleep(1)
        self.saldo += valor

        print("Depósito realizado com sucesso!")
        print("-"*45)

    def sacar(self):
        print("-"*45)
        while True:
            try:
                valor = float(input("Informe o valor a sacar: "))
                break
            except (ValueError, KeyboardInterrupt):
                print("Valor inválido. Caso queira adicionar casa decimais utilize pontos (\".\") para separar as casas.\n"
                      "Se não, utilize apenas números.\n")
                sleep(1)
        
        sleep(1)
        if valor < 0:
            print(f"Valores negativos não são permitidos. Alternando para R${valor * -1}.")
            valor = valor * -1
        elif valor == 0:
            print("O valor nulo não é permitido.")

        if valor > self.saldo and valor > 0:
            print("Saldo Insuficente!")

            if self.saldo == 0:
                usar_limite = input("Usar saldo especial? [S/N] ").upper().strip()[0]
                while usar_limite not in 'SN':
                    usar_limite = input("Opção Inválida. Usar saldo especial? [S/N] ").upper().strip()[0]

                if usar_limite == 'S':
                    if valor > self.limite:
                        print("O valor ultrapassa o limite.")
                    else:    
                        print("Saque aprovado pelo banco!")
                        sleep(1)
                        print("Imprimindo...")
                        self.limite -= valor
                        sleep(2)
                        print("Saque realizado com sucesso!")
                else:
                    print("Operação cancelada.")
            
            elif (valor - self.saldo) < self.limite:
                usar_limite = input("Usar saldo especial para completar o saque? [S/N] ").upper().strip()[0]
                while usar_limite not in 'SN':
                    usar_limite = input("Opção Inválida. Usar saldo especial? [S/N] ").upper().strip()[0]

                if usar_limite == 'S':   
                    print("Saque aprovado pelo banco!")
                    sleep(1)
                    print("Imprimindo...")
                    valor -= self.saldo
                    self.saldo = 0
                    self.limite -= valor 
                    sleep(2)
                    print("Saque realizado com sucesso!")
                else:
                    print("Operação cancelada.")      
        
        elif valor > 0:
            print("Saque aprovado pelo banco!")
            sleep(1)
            print("Imprimindo...")
            self.saldo -= valor
            sleep(2)
            print("Saque realizado com sucesso!")
        
        print("-"*45)
        sleep(1)

    def emprestimo(self):
        print("-"*45)
        print(f"{'EMPRESTIMO':^45}")
        print("-"*45)
        while True:
            try:
                acesso = int(input("\n1- Realizar Empréstimo"
                                   "\n2- Pagar Empréstimo"
                                   "\n3- Voltar"
                                   "\nSelecione: "))
                break
            except (ValueError, KeyboardInterrupt):
                print("Valor inválido. Selecione uma das operações listadas.\n")
                sleep(1)
                
        if acesso == 1:
            print("-"*45)
            while True:
                try:
                    acesso = int(input("\nGostaria de realizar um empréstimo pessoal?"
                                       "\nInformações: Prazo para pagamento de 12 meses com juros de 2% ao mês."
                                       "\n1- Sim"
                                       "\n2- Não"
                                       "\nSelecione: "))
                    break
                except (ValueError, KeyboardInterrupt):
                    print("Valor inválido. Selecione uma das operações listadas.\n")
                    sleep(1)
            sleep(1)

            if self.tem_emprestimo == True:
                print("\nVocê não pode realizar outro empréstimo até que o anterior seja pago.")
                sleep(1.5)
            elif acesso == 1:
                print("-"*45)
                while True:
                    try:
                        valor = int(input("\nValores disponíveis:"
                                           "\n1- R$5.000"
                                           "\n2- R$10.000"
                                           "\n3- R$25.000"
                                           "\n4- R$50.000"
                                           "\n5- R$100.000"
                                           "\nSelecione: "))
                        break
                    except (ValueError, KeyboardInterrupt):
                        print("Valor inválido. Selecione uma das operações listadas.\n")
                        sleep(1)
                print("-"*45)

                sleep(1)
                if valor == 1:
                    print("Realizando transação...")
                    self.saldo += 5000
                    self.tem_emprestimo = True
                    self.valor_emprestimo = 5000
                    self.parcelas = 12
                    sleep(1)
                    print("Empréstimo realizado! Fique atento às datas de pagamento.")
                if valor == 2:
                    print("Realizando transação...")
                    self.saldo += 10000
                    self.tem_emprestimo = True
                    self.valor_emprestimo = 10000
                    self.parcelas = 12
                    sleep(1)
                    print("Empréstimo realizado! Fique atento às datas de pagamento.")
                if valor == 3:
                    print("Realizando transação...")
                    self.saldo += 25000
                    self.tem_emprestimo = True
                    self.valor_emprestimo = 25000
                    self.parcelas = 12
                    sleep(1)
                    print("Empréstimo realizado! Fique atento às datas de pagamento.")
                if valor == 4:
                    print("Realizando transação...")
                    self.saldo += 50000
                    self.tem_emprestimo = True
                    self.valor_emprestimo = 50000
                    self.parcelas = 12
                    sleep(1)
                    print("Empréstimo realizado! Fique atento às datas de pagamento.")
                if valor == 5:
                    print("Realizando transação...")
                    self.saldo += 100000
                    self.tem_emprestimo = True
                    self.valor_emprestimo = 100000
                    self.parcelas = 12
                    sleep(1)
                    print("Empréstimo realizado! Fique atento às datas de pagamento.")
                sleep(1.5)
            
            elif acesso != 2:
                print("Opção não encontrada. Retornando...")
                sleep(1)
            print("-"*45)
            
        elif acesso == 2:
            print("-"*45)
            sleep(1)
            if self.tem_emprestimo == False:
                print("Você não possui dívidas com banco! Continue assim ;)")
                sleep(1.5)
            else:
                    print("-"*45)
                    sleep(1.5)
                    valor_parcela = (self.valor_emprestimo / 12) + (self.valor_emprestimo * 0.02)
                    print(f"\nValor da parcela: R${valor_parcela:.2f}")
                    print(f"Parcelas restantes: {self.parcelas} parcelas")

                    while True:
                        try:
                            acesso = int(input("\n1- Pagar parcela atual"
                                               "\n2- Amortizar parcelas"
                                               "\n3- Voltar"
                                               "\nSelecione: "))
                            break
                        except (ValueError, KeyboardInterrupt):
                            print("Valor inválido. Selecione uma das operações listadas.\n")
                            sleep(1)
                        
                    if acesso == 1:
                        if valor_parcela > self.saldo:
                            print("Saldo Insuficente!")

                            if self.saldo == 0:
                                usar_limite = input("Usar saldo especial? [S/N] ").upper().strip()[0]
                                while usar_limite not in 'SN':
                                    usar_limite = input("Opção Inválida. Usar saldo especial? [S/N] ").upper().strip()[0]

                                if usar_limite == 'S':
                                    if valor_parcela > self.limite:
                                        print("O valor ultrapassa o limite.")
                                    else:    
                                        sleep(1)
                                        self.limite -= valor_parcela
                                        self.parcelas -= 1
                                        print("Pagamento realizado!")

                                else:
                                    print("Operação cancelada.")
                            
                            elif (valor_parcela - self.saldo) < self.limite:
                                usar_limite = input("Usar saldo especial para completar o saque? [S/N] ").upper().strip()[0]
                                while usar_limite not in 'SN':
                                    usar_limite = input("Opção Inválida. Usar saldo especial? [S/N] ").upper().strip()[0]

                                if usar_limite == 'S':   
                                    sleep(1)
                                    valor_parcela -= self.saldo
                                    self.saldo = 0
                                    self.limite -= valor_parcela
                                    self.parcelas -= 1
                                    print("Pagamento realizado!")
                                else:
                                    print("Operação cancelada.")
                        else:
                            sleep(1)
                            self.saldo -= valor_parcela
                            self.parcelas -= 1
                            print("Pagamento realizado!")
                        sleep(1.5)
                    elif acesso == 2:
                        print("-"*42)
                        while True:
                            try:
                                quantidade = int(input("Informe o número de parcelas a pagar: "))             
                                break
                            except (ValueError, KeyboardInterrupt):
                                print("Valor inválido. Selecione uma das operações listadas.\n")
                                sleep(1)                   
                        
                        if quantidade > self.parcelas:
                            quantidade = self.parcelas
                            print(f"O máximo que você pode escolher no momento é {quantidade}.")
                        
                        print(f"\nValor de {quantidade} parcelas: R${valor_parcela*quantidade:.2f}")
                        valor_parcela *= quantidade

                        confirma = input("Pagar? [S/N] ").upper().strip()[0]
                        while confirma not in 'SN':
                            confirma = input("Opção Inválida. Deseja pagar agora este valor? [S/N] ").upper().strip()[0]
                            
                        if confirma == 'S': 
                            if valor_parcela > self.saldo:
                                print("Saldo Insuficente!")
                            
                                if self.saldo == 0:
                                    usar_limite = input("Usar saldo especial? [S/N] ").upper().strip()[0]
                                    while usar_limite not in 'SN':
                                        usar_limite = input("Opção Inválida. Usar saldo especial? [S/N] ").upper().strip()[0]

                                    if usar_limite == 'S':
                                        if valor_parcela > self.limite:
                                            print("O valor ultrapassa o limite.")
                                        else:    
                                            sleep(1)
                                            self.limite -= valor_parcela
                                            self.parcelas -= quantidade
                                            print("Pagamento realizado!")
                                    else:
                                        print("Operação cancelada.")
                                
                                elif (valor_parcela - self.saldo) < self.limite:
                                    usar_limite = input("Usar saldo especial para completar o saque? [S/N] ").upper().strip()[0]
                                    while usar_limite not in 'SN':
                                        usar_limite = input("Opção Inválida. Usar saldo especial? [S/N] ").upper().strip()[0]

                                    if usar_limite == 'S':   
                                        sleep(1)
                                        valor_parcela -= self.saldo
                                        self.saldo = 0
                                        self.limite -= valor_parcela
                                        self.parcelas -= quantidade
                                        print("Pagamento realizado!")
                                    else:
                                        print("Operação cancelada.")
                            else:
                                sleep(1)
                                self.saldo -= valor_parcela
                                self.parcelas -= quantidade
                                print("Pagamento realizado!")
                        else:
                            print("Operação cancelada.")
                        sleep(1.5)
                    elif acesso == 3:
                        print("Retornando...")
                    
                    else:
                        print("Opção não encontrada.\n")
                        sleep(1)

            if self.parcelas == 0:
                self.tem_emprestimo = False
        
        elif acesso == 3:
            print("Retornando...")
                    
        else:
            print("Opção não encontrada.\n")
            sleep(1) 
        
        print("-"*45)

    def tranferir_para_poupanca(self, cliente_poupanca):
        print("-"*45)
        print(f"{'TRANSFERENCIA':^45}")
        print("-"*45)
        print("Transfira seu dinheiro para outra conta em seu nome.")
        print("Tipo atual: Corrente.\n"
              "Conta alternativa: Poupança")
        print(f"Seu saldo: R${self.saldo}\n")
        while True:
            try:
                confirma = int(input("Deseja tranferir seu saldo?"
                                       "\n1- Sim"
                                       "\n2- Não"
                                       "\nSelecione: "))
                break
            except (ValueError, KeyboardInterrupt):
                print("Valor inválido. Selecione uma das operações listadas.\n")
                sleep(1)
        
        if confirma == 1:
            while True:    
                while True:
                    try:
                        ID = int(input("Confirme o ID de sua Conta Poupança: "))
                        break
                    except (ValueError, KeyboardInterrupt):
                        print("Valor inválido. Digite corretamente o ID.\n")
                        sleep(1)

                if str(ID) == cliente_poupanca.id:
                    while True:
                        try:
                            valor = int(input("Valor a transferir: "))
                            break
                        except (ValueError, KeyboardInterrupt):
                            print("Valor inválido. Caso queira adicionar casa decimais utilize pontos (\".\") para separar as casas.\n"
                        "Se não, utilize apenas números.\n")
                            sleep(1)
                    
                    sleep(1)
                    if valor < 0:
                        print(f"Valores negativos não são permitidos. Alternando para R${valor * -1}.")
                        valor = valor * -1

                    if valor <= self.saldo:
                        print("Transferindo...")
                        sleep(2)
                        self.saldo -= valor
                        cliente_poupanca.saldo += valor
                        print("Transferência realizada!")
                        sleep(1)
                        break
                    else:
                        print("Saldo Insuficiente!")
                        sleep(1)
                        break
                else:
                    print("ID incorreta.")
                    sleep(1)
                    tentar_id = input("Tentar novamente? [S/N] ").upper().strip()[0]
                    while tentar_id not in 'SN':
                        tentar_id = input("Opção Inválida. Tentar novamente? [S/N] ").upper().strip()[0]
                    
                    if tentar_id == 'N':
                        break
        elif confirma == 2:
            print("Retornando...")
            sleep(1)
        else:
            print("Opção Inválida.")           
                
        print("-"*45) 
