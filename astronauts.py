# from pprint import pprint
# import statistics
# from collections import Counter


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
    return darabszamok


def szazalekolo(ertek, osszes):
    return round(ertek/osszes*100, 1)


def main():
    melyik_mennyi = []
    sorba_rendezett = sorba_renedzo(elemek_darabszama(megkapja_honapok(beolvaso())))
    for szamlalo in enumerate(elemek_darabszama(megkapja_honapok(beolvaso())), 1):
        melyik_mennyi.append(szamlalo)
    elso = sorba_rendezett[0]
    masodik = sorba_rendezett[1]
    harmadik = sorba_rendezett[2]
    szam = 0
    while szam != 12:
        if (szam, elso) == melyik_mennyi[szam-1]:
            print(f'Az év {szam}. hónapjában született a legtöbb űrhajós,')
        if (szam, masodik) == melyik_mennyi[szam-1]:
            print(f'Az év {szam}. hónapjában született a második legtöbb űrhajós.')
        if (szam, harmadik) == melyik_mennyi[szam - 1]:
            print(f'Az év {szam}. hónapjában született a harmadik legtöbb űrhajós.')
        szam += 1
    print(f'Az asztronauták {szazalekolo(elso, sum(sorba_rendezett))}%-a augusztusban született. ')
    print(f'Az asztronauták {szazalekolo(masodik, sum(sorba_rendezett))}%-a májusban született. ')
    print(f'Az asztronauták {szazalekolo(harmadik, sum(sorba_rendezett))}%-a októberben született. ')


main()
