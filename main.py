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
    for start in range(0, len(lst) + 1):
        for end in range(start + 1, len(lst) + 1):
            if doar_elem_pp(lst[start:end]):
                lista_secvente.append(lst[start:end])


    secv_max = []
    for secventa in lista_secvente:
        if(len(secventa) > len(secv_max)):
            secv_max = secventa
    return secv_max


def nr_de_biti_unu(n):
    '''
    Transforma un numar din baza 10 in baza 2 si retine intr-un contor aparitiile bit-ului 1
    '''
    contor = 0
    n2 = int(n)
    while n2 > 0:
        if n2 % 2 == 1:
            contor += 1
        n2 = n2 // 2
    return contor


def test_nr_biti():
    assert nr_de_biti_unu(23) == 4
    assert nr_de_biti_unu(1000) == 6
    assert nr_de_biti_unu(4755) == 6
    assert nr_de_biti_unu(2) == 1
    assert nr_de_biti_unu(11+33) == 3
    assert nr_de_biti_unu(102*67) == 7
    assert nr_de_biti_unu(56) == 3
    assert nr_de_biti_unu(9999) == 8


def all_same_bit(lst):
    '''
    verifica daca toate elementele unei liste au acelasi numar de biti unu
    '''
    test_nr_biti()
    cont = nr_de_biti_unu(lst[0])
    for i in lst:
        if nr_de_biti_unu(i) != cont:
            return False
    return True


def get_longest_same_bit_counts(lst):
    '''
    :param lst: -o lista de numere
    :return:  -cea mai lunga lista de numere dupa criteriul de la problema 11
    '''
    lista_secvente = []
    for start in range(0, len(lst) + 1):
        for end in range(start + 1, len(lst) + 1):
            if all_same_bit(lst[start:end]):
                lista_secvente.append(lst[start:end])

    secv_max =[]
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
        elif optiune == '3':
            print(get_longest_same_bit_counts(lista))
        elif optiune == 'x':
            break

main()
