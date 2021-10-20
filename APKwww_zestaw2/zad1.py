#zad1
def merge(lista_a, lista_b):
    i=len(lista_a)-1
    j=0
    wynik = []
    while(i > -1):
        if(i%2 == 0):
            wynik.append(lista_a[i])
            j=j+1
        i=i-1

    i=len(lista_b)-1
    while(i > -1):
        if(i%2 == 1):
            wynik.append(lista_b[i])
            j=j+1
        i=i-1
    print(wynik)

lista_a=["a", "b", "c"]
lista_b=[1, 2, 3, 8, 9, 10]
merge(lista_a, lista_b)