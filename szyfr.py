# Proszę napisać program który będzie szyfrować i deszyfrować tekst za pomocą kody Cezara.
# Proszę uwzględnić możliwość zmiany przesunięcia(standardowo 2).
# https: // pl.wikipedia.org / wiki / Szyfr_Cezara

def szyfrowanie(ciag_wejsciowy, numer):
    ciag_wyjsciowy = ""
    for znak in ciag_wejsciowy:
        if ((ord(znak) > 96) & (ord(znak) < 123 - numer)):
            ciag_wyjsciowy += (chr(ord(znak) + numer))
        elif ((ord(znak)) >= 123 - numer):
            ciag_wyjsciowy += (chr(ord(znak) + numer - 26))
        else:
            ciag_wyjsciowy += znak
    print("ciag zaszyfrowany\n" + ciag_wyjsciowy)
    return ciag_wyjsciowy


def deszyfrowanie(ciąg_wejsciowy, numer):
    ciag_wyjsciowy = ""
    for znaki in ciąg_wejsciowy:
        if ((ord(znaki) > 96 + numer) & (ord(znaki) < 123)):
            ciag_wyjsciowy += (chr(ord(znaki) - numer))
        elif ((ord(znaki)) > 96):
            ciag_wyjsciowy += (chr(ord(znaki) - numer + 26))
        else:
            ciag_wyjsciowy += znaki
    print("ciag zdeszyfrowany:\n" + ciag_wyjsciowy)

numer = int(input("Podaj liczbę przesunięcia:"))
znaki = str.lower(input("Wpisz tekst:"))
deszyfrowanie(szyfrowanie(znaki, numer), numer)