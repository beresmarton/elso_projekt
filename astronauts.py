from pprint import pprint
def beolvaso():
    egy_szemely_adatai = []
    szuletesi_datumok = []
    with open('astronauts.csv.csv') as forras:
        forras.readline()
        for sor in forras:
            adatsor = sor.strip().split(',')
            egy_szemely_adatai.append(adatsor)
        for szemely in egy_szemely_adatai:
            szuletesi_datum = szemely[4]
            szuletesi_datumok.append(szuletesi_datum)
        return szuletesi_datumok

def megkapja_honapok(lista):
    honapok = []
    for elem in lista:
        elem = elem.split('/')
        honapok.append(elem[0])
    pprint(honapok)



megkapja_honapok(beolvaso())
