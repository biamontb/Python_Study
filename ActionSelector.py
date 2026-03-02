# entrar, sentar, correr
opcao = -1 # para garantir que o while execute pelo menos uma vez.

while opcao != 0: # O laço só continua enquanto opcao for diferente de 0.
        opcao = int(input("[1] Entrar \n[2] Sentar \n[3] Correr \n[0] Sair \n: "))

        if opcao == 1:
                print("Entrando...")
        elif opcao == 2:
                print("Sentando...")
        elif opcao == 3:
                print("Correndo...")