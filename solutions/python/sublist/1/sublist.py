# Definição das constantes que o Exercism precisa para os testes
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def is_sublist(lista_menor, lista_maior):
    """Função auxiliar para verificar se uma lista menor está contida em uma maior"""
    if not lista_menor:  # Uma lista vazia é sempre sublista de qualquer outra
        return True
        
    tam_menor = len(lista_menor)
    tam_maior = len(lista_maior)
    
   
    for i in range(tam_maior - tam_menor + 1):
        if lista_maior[i : i + tam_menor] == lista_menor:
            return True
            
    return False


def sublist(list_one, list_two):
   
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL