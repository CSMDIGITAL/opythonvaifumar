print("Menu Finaceiro")
print("1 - Cadastrar")
print("2 - Listar")
print("3 - Atualizar")
print("4 - Excluir")

opcao = int(input("Digite a opcâo"))

if opcao == 1:
    print("Você escolheu CADASTRAR")
    # aqui entraria a lógica de cadastro
elif opcao == 2:
    print("Você escolheu LISTAR")
    # lógica de listagem
elif opcao == 3:
    print("Você escolheu ATUALIZAR")
    # lógica de atualização
elif opcao == 4:
    print("Você escolheu EXCLUIR")
    # lógica de exclusão
else:
    print("Opção inválida! Escolha entre 1 e 4.")