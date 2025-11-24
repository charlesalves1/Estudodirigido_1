idade = int(input("Qual a sua idade? ")) 
cidade = input("Qual a sua cidade? ")
if idade >= 60: 
    print("Você é idoso e mora {cidade}.") 
elif idade >= 18: 
    print("Você é adulto e mora {cidade}.") 
else: 
    print("Você é menor de idade e mora {cidade}.")
    print(f"Você tem {idade} anos e mora em {cidade}.")