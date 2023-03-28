from conta import *
from time import sleep

class ContaPoupanca(Conta):
    def __init__(self, id, saldo):
        super().__init__(id, saldo)
        self.taxa_de_rendimento = 0.475

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
        else:
            print("Saque aprovado pelo banco!")
            sleep(1)
            print("Imprimindo...")
            self.saldo -= valor
            sleep(2)
            print("Saque realizado com sucesso!")
        
        print("-"*45)

    def verificar_rendimento(self):
        print("-"*45)
        sleep(1)
        if self.saldo > 0:  
            while True:
                tempo = input("Digite o tempo para calcular o investimento (Ex.: 6 meses; 1 ano; 8 dias): ").lower().split()
                sleep(1)

                if len(tempo) != 2:
                    erro = True
                    print("Digite corretamente os dados.\n")
                    sleep(1)
                else:
                    try:
                        tempo[0] = int(tempo[0])
                    except ValueError:
                        erro = True
                        print("Digite um valor válido para o tempo.\n")
                    else:
                        erro = False
                        tempo[0] = str(tempo[0])

                if erro == False:
                    if (tempo[1] == "segundo") or (tempo[1] == "segundos"):
                        tempo_de_rendimento = int(tempo[0]) / (365 * 24 * 60 * 60)
                        break
                    elif (tempo[1] == "minutos") or (tempo[1] == "minutos"):
                        tempo_de_rendimento = int(tempo[0]) / (365 * 24 * 60)
                        break
                    elif (tempo[1] == "hora") or (tempo[1] == "horas"):
                        tempo_de_rendimento = int(tempo[0]) / (365 * 24)
                        break
                    elif (tempo[1] == "dia") or (tempo[1] == "dias"):
                        tempo_de_rendimento = int(tempo[0]) / 365
                        break
                    elif (tempo[1] == "semana") or (tempo[1] == "semanas"):
                        tempo_de_rendimento = int(tempo[0]) / (365 / 7)
                        break
                    elif (tempo[1] == "mes") or (tempo[1] == "mês") or (tempo[1] == "meses"):
                        tempo_de_rendimento = int(tempo[0]) / 12
                        break
                    elif (tempo[1] == "ano") or (tempo[1] == "anos"):
                        tempo_de_rendimento = int(tempo[0])
                        break
                    else:
                        print("Digite uma unidade de tempo válida.\n")
                        sleep(1)
                        

            rendimento = self.saldo * (1 + self.taxa_de_rendimento) ** tempo_de_rendimento - self.saldo

            sleep(1)
            print(f"Seu rendimento em {' '.join(tempo)} será de R${rendimento:.2f}.\n"
                f"Totalizando R${(self.saldo + rendimento):.2f} ao fim do período estimado.")
        
        else:
            print("Você não possui saldo. Adicione para começar a render.")
        
        print("-"*45)
        sleep(1.5)
        input("Aperte ENTER para continuar.")

    def tranferir_para_corrente(self, cliente_corrente):
        print("-"*45)
        print(f"{'TRANSFERENCIA':^45}")
        print("-"*45)
        print("Transfira seu dinheiro para outra conta em seu nome.")
        print("Tipo atual: Poupança.\n"
              "Conta alternativa: Corrente")
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
                    
                if str(ID) == cliente_corrente.id:
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
                        cliente_corrente.saldo += valor
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
                