import math


def citire_lista():
    '''
    elementele se introduc separate prin cate un spatiu
    '''
    str_lst = input("Introduceti elementele : ")
    str_elem = str_lst.split(" ")
    result_lst = []
    for str_elem in str_elem:
        elem = int(str_elem)
        result_lst.append(elem)
    return result_lst

def doar_elem_pp(lst):
    '''
    verifica daca o lista data contine sau nu
    doar numere patrate perfecte
    '''
    for element in lst:
        if math.sqrt(element) * math.sqrt(element) != element:
            return False
    return True


def get_longest_all_perfect_squares(lst):
    '''
    gaseste cea mai lunga secventa de patrate perfecte
    '''
    lista_secvente = []
    #lista[start:end]
    for start in range(0, len(lst)):
        for end in range(start + 1, len(lst)):
            if doar_elem_pp(lst[start:end]):
                lista_secvente.append(lst[start:end])


    secv_max = []
    for secventa in lista_secvente:
        if(len(secventa) > len(secv_max)):
            secv_max = secventa
    return secv_max



def main():
    while True:
        print('1.Citire lista.')
        print('2.Determina cea mai lunga secventa de patrate perfecte.')
        print('3.Determina cea mai lunga secventa de numere cu acelasi numar de biti in reprezentarea binara.')
        print('x.Iesire.')
        optiune = input('Selectati optiunea : ')
        if optiune == '1':
            lista = citire_lista()
            print(lista)
        elif optiune == '2':
            print(get_longest_all_perfect_squares(lista))
        elif optiune == 'x':
            break

main()
