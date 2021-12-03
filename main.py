# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    num = int(input("Escriu el numero de notes que vols introduir"))
    mitjasuspes = 0
    mitjaaprovats = 0
    quantitatsuspes = 0
    quantitataprovat = 0
    i= 0
    while i != num:
        nota = int(input("Quina nota has tret?: "))
        i += 1
        while nota < 0 or nota > 10:
            print ("Error")
            nota = int(input("Quina nota has tret?: "))
        if nota >= 5:
            quantitataprovat += 1
            mitjaaprovats = mitjaaprovats + nota
        else:
            quantitatsuspes += 1
            mitjasuspes = mitjasuspes + nota
    if quantitataprovat > 0:
        print("La mitja dels aprovats és: ", mitjaaprovats/quantitataprovat)
        print("La quantitat d'aprovats és: ", quantitataprovat)
    else:
        print("No ha aprovat ningú")
    if quantitatsuspes > 0:
        print("La mitja dels suspesos és: ", mitjasuspes / quantitatsuspes)
        print("La quantitat de suspesos és: ",quantitatsuspes)
    else:
        print("No ha suspés ningú")
if __name__ == '__main__':
    main()
