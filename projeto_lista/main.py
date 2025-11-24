from funcoes import cadastrar, listar 
 
itens = [] 
 
while True: 
    print("\n[1] Cadastrar  [2] Listar  [0] Sair") 
    op = input("Escolha: ").strip() 
 
    if op == "1": 
        nome = input("Item: ").strip() 
        cadastrar(itens, nome) 
    elif op == "2": 
        listar(itens) 
    elif op == "0": 
        break 
    else: 
        print("Opção inválida.")