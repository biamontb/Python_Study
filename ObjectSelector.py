# Seus itens: Lápis, Mesa, Celular.
opcao = -1 # para garantir que o while execute pelo menos uma vez.

while opcao != 0: # O laço só contina enquanto opcao for diferente de 0.
        opcao = int(input("[1] Lápis \n[2] Mesa\n[3] Celular\n[0] Sair\n"))

        if opcao == 1:
                print("Você pegou o Lápis.")
        elif opcao == 2:
                print("Você pegou a Mesa.")
        elif opcao == 3:
                print("Você pegou o Celular")