#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from clp3 import clp
def czy_liczba(znak):
    if(znak == "0" or
        znak == "1" or
        znak == "2" or
        znak == "3" or
        znak == "4" or
        znak == "5" or
        znak == "6" or
        znak == "7" or
        znak == "8" or
        znak == "9"):
        return True
    return False
def sama_liczba(ciag):
    ret = ""
    for it in ciag:
        if czy_liczba(it):
            ret += it
    return ret

def czy_litera(znak):
    z = ord(znak)
    if (z == ord("ą") or z == ord("Ą") or
            z == ord("ć") or z == ord("Ć") or
            z == ord("ś") or z == ord("Ś") or
            z == ord("ę") or z == ord("Ę") or
            z == ord("ł") or z == ord("Ł") or
            z == ord("ń") or z == ord("Ń") or
            z == ord("ó") or z == ord("Ó") or
            z == ord("ź") or z == ord("Ź") or
            z == ord("ż") or z == ord("Ż")):
        return True

    if ((z >= ord("a") and z <= ord("z")) or (z <= ord("Z") and z >= ord("A"))):
        return True
    return False
def czy_skrot(zdanie):
    if len(zdanie) < 5: return False
    sktot = zdanie[-4:]
    if sktot == ' ul.' or \
        sktot == ' zł.' or\
        sktot == 'ang.' or\
        sktot == 'rys.' or\
        sktot == 'itd.' or\
        sktot == 'itp.' or\
        sktot == 'tzw.' or\
        sktot == ' pt.' or\
        sktot == 'tzn.':
        return True
    sktot = zdanie[-5:]
    if sktot == 'm.in.' or \
        sktot == 'proc.':
        return True
    sktot = zdanie[-3:]
    if sktot == 'np.' or \
        sktot == ' w.'or \
        sktot == ' r.' or \
        sktot == 'in.' or \
        sktot == ' m.' or \
        sktot == '...':
        return True
    sktot = zdanie[-2:]
    if sktot == '..': return  False
    return False
def podziel_na_zdania(tekst):

    ret_zdania = []
    zdanie = ""
    for indeks, znak in enumerate(tekst):
        zdanie += znak
        if znak == "?" or znak == "!":
            ret_zdania.append(zdanie)
            zdanie = ""
        if znak == ".":
            if indeks + 1 < len(tekst):
                if tekst[indeks + 1] == '.': continue
            if not czy_skrot(zdanie):
                ret_zdania.append(zdanie)
                zdanie = ""

    return ret_zdania
def samo_slowo(s):
    ret = ""
    for it in s:
        if(czy_litera(it)):
            ret += it
    return ret

def przygotuj_tekst(plik):
    #plik = plik.lower()
    tekst = ""

    '''skróty'''
    plik = plik.replace(' ul.', ' ul')
    plik = plik.replace(' zł.', ' zł')
    plik = plik.replace(' ok.', ' ok')
    plik = plik.replace('m.in.', 'm in')
    plik = plik.replace('tzn.', 'tzn')
    plik = plik.replace('tzw.', 'tzw')
    plik = plik.replace('np.', 'np')
    plik = plik.replace(' r.', ' r')
    plik = plik.replace('ang.', 'ang')
    plik = plik.replace('proc.', 'proc')
    plik = plik.replace('rys.', 'rys')
    plik = plik.replace('itd.', 'itd')
    plik = plik.replace('itp.', 'itp')
    plik = plik.replace(' w.', ' w')
    plik = plik.replace(' pt.', ' pt')

    '''interpunkcja i puste znaki'''
    plik = plik.replace('\n', ' ')
    plik = plik.replace('  ', ' ')
    plik = plik.replace('   ', ' ')
    plik = plik.replace('?', '.')
    plik = plik.replace('!', '.')
    plik = plik.replace('...', '..')
    plik = plik.replace('..', '.')
    plik = plik.replace('.', '.\n')
    plik = plik.replace('.\n ', '.\n')

    for it in plik:
        if czy_litera(it) or it == ',' or it == ' ' or it == '.' or it == '(' or it == ')' or it == '\n':
            tekst += it
        continue
    return tekst

def randomizacja():
    losowy = list(range(100))
    random.shuffle(losowy)
    return losowy

def wczytaj_teksty_losowo():
    teksty = open("input/teksty.txt", "w", encoding='utf8')
    for file in randomizacja():
        tekst = "############# " + str(file) + " #############"
        sciezka_do_pliku = "input/" + str(file) + ".txt"
        plik = open(sciezka_do_pliku, "r", encoding='utf8').read()
        plik = przygotuj_tekst(plik)

        teksty.write((tekst + '\n' + plik + '\n'))
    teksty.close()

def wczytaj_teksty():
    teksty = open("input/teksty.txt", "w", encoding='utf8')
    for file in range(100):
        tekst = "############# " + str(file) + " #############"
        sciezka_do_pliku = "input/" + str(file) + ".txt"
        plik = open(sciezka_do_pliku, "r", encoding='utf8').read()
        plik = przygotuj_tekst(plik)

        teksty.write((tekst + '\n' + plik + '\n'))
    teksty.close()

def mianownik(wyraz):
    id = clp(wyraz)
    if len(id) > 0:
        list_p = clp.forms(id[0])
        if len(list_p) > 0:
            return list_p[0]
    return wyraz

def podstawowa_forma(wyraz):
    return mianownik(wyraz)
#wczytaj_teksty_losowo()
def odmiana_wyrazu_clp(wyraz):
    odmiany = []
    id = clp(wyraz)
    for it in range(len(id)):
        odmiany += clp.forms(id[it])
    return odmiany