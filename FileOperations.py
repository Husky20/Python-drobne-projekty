def loadFile(file_name, file_extension):
    '''
     Odczyt plików niezależnie od rozszerzenia
    :param file_name: nazwa pliku
    :param file_extension: rozszerzenie pliku
    :return: treść pliku
    '''
    if("." in file_extension):
        file = open((str(file_name + file_extension)), encoding="utf-8").read()
    else:
        file = open((str(file_name) + "." + str(file_extension)), encoding="utf-8").read()
    return file

def saveFile(file_name, file_extension, contents):
    '''
     Zapis do plików
    :param file_name: nazwa pliku
    :param file_extension: rozszerzenie pliku
    :param contents: treść do wpisania do pliku
    '''
    file = open(str(file_name + file_extension), "w")
    file.write(contents)
    file.close()

def readClearText(file_name, file_extension):
    '''
    Funkcja odczytuje tekst i wyrzuca z niego wszystko co nie jest literą ani spacją
    :param s: sciężka do pliku
    :return: string zawierający jedynie małe litery i pojedńcze spacje
    '''
    return onlyLetter(loadFile(file_name + file_extension).lower())


def onlyLetter(s):
    '''
    :param s: String który zawiera w sobie zadany tekst
    :return: zwraca przyjęty tekst zawierający jedynie litery oraz pojedyńcze spacje
    entery są zamienione na pojedyńcze spacje
    '''
    ret = ""
    s = s.replace("\n", " ")
    while "  " in s:
        s = s.replace("  ", " ")
    for x in s:
        if orALetter(x) or x == " ":
            ret += x
    return ret


def orALetter(ch):
    '''
    :param ch: znak(mała litera) do analizy polskiego alfabetu
    :return: wartość binarna czy znak należy do polskiego alfabetu
    '''
    z = ord(ch)
    if ch in "ąćęłńóśźż":
        return True

    if z >= ord("a") and z <= ord("z"):
        return True
    return False


def orAInt(ch):
    '''
    :param ch: pojedyńczy znak znak
    :return: wartość binarna określająca czy znak jest cyfrom
    '''
    return ch in "0123456789"
