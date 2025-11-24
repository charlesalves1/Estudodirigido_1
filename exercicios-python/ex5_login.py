senha_correta = "python123"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    tentativa = input("Digite a senha: ")

    if tentativa == senha_correta:
        print("Acesso liberado!")
        break
    else:
        tentativas += 1
        print("Senha incorreta!")

if tentativas == max_tentativas:
    print("Acesso bloqueado!")
