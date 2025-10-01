import msvcrt

def limpar_buffer():
    while msvcrt.kbhit():  # Enquanto houver teclas no buffer
        msvcrt.getch()     # Consome a tecla

# Exemplo de uso
print("Digite algo: ")
texto = input()
limpar_buffer()  # Limpa o buffer
print("Buffer limpo, digite novamente: ")
texto_novo = input()
