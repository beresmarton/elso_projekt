# from pprint import pprint
# import statistics


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
        honapok.append(int(elem[0]))
    return honapok


def elemek_darabszama(szamok):
    gyakorisag = []
    for szam in range(1, 13):
        adott_szam = szamok.count(szam)
        gyakorisag.append(adott_szam)
    return gyakorisag


def sorba_renedzo(darabszamok):
    darabszamok.sort(reverse=True)
    print(darabszamok)


def main():
    melyik_mennyi = []
    for szamlalo in enumerate(elemek_darabszama(megkapja_honapok(beolvaso())), 1):
        melyik_mennyi.append(szamlalo)
    print(melyik_mennyi)
    sorba_renedzo(elemek_darabszama(megkapja_honapok(beolvaso())))


main()
