def cadastrar(lista, item):
    if item in lista:
        print("Este item já está cadastrado!")
    else:
        lista.append(item)
        print("Item cadastrado!")


def listar(lista):
    if not lista:
        print("Lista vazia.")
    else:
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")


def remover(lista, numero):
    if 1 <= numero <= len(lista):
        removido = lista.pop(numero - 1)
        print(f"Item removido: {removido}")
    else:
        print("Número inválido!")
