num1 = int(input("Digite o primeiro número: ")) 
num2 = int(input("Digite o segundo número: ")) 
resultado = num1 + num2 
print(f"A soma é {resultado}")
subtracao = num1 - num2
multiplicacao = num1 * num2
print(f"A subtração é {subtracao}")
print(f"A multiplicação é {multiplicacao}")
if num2 != 0:
    divisao = num1 / num2
    print(f"A divisão é {divisao}")
else:
    print("Divisão por zero não é possível")