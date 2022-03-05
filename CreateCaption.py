'''
2. Tworzenie napisu - CreateCaption
    a. Mamy firmę która zajmuję się tworzeniem liter z drewna podobnych do napisu. Zgłosiła się do nas klientka,
    która chce wystawić wiele napisów z nazwą swojej firmy, lecz zależy jej na czasie przez co przysyła nam kilka potencjalnych nazw swojej przyszłej firmy.
    b. Napisz program, który na wejściu dostanie dwie wartości
        i. Ciąg znaków zawierający litery na stanie np.: „TTOQWERTTBOBBBBZC”
        ii. Listę ciągów znaków zawierających potencjalne nazwy firmy np.:[„TOMI”, „BOMBKI”]
    c. Na wyjściu musi zawierać się wartość „int”, która stanowi największą możliwą ilość wygenerowanych nazw firmy
    tzn. jeżeli da się wygenerować jedną nazwę 3x, a drugą 2x to zwracamy „3”, jeżeli dwie nazwy da się wygenerować 3x to zwracamy „3”
'''

def dictLetters(letters):
    dict_letters = {}
    for it in letters:
        if it in dict_letters: dict_letters[it] += 1
        else: dict_letters[it] = 1
    sorted(dict_letters.items(), key=lambda kv: kv[1], reverse=True)
    return dict_letters

def listDict(example_names):
    list_dict = []
    for name in example_names:
        list_dict.append(dictLetters(name))
    return list_dict


def createcaption0(letters, example_names):
    list_lists = []
    dict_letters = dictLetters(letters)
    list_dict = listDict(example_names)

    for dict in list_dict:
        list_p = []
        for letter1 in dict_letters :
            for letter2 in dict:
                if letter1 == letter2:
                    list_p.append(int(dictLetters(letters)[letter1]/dict[letter2]))
        if len(list_p) != len(dict.items() ):
            continue


        list_lists.append(min(list_p))

    return max(list_lists)

def createcaption1(letters, example_names):
    dict_letters = dictLetters(letters)
    list_dict = listDict(example_names)
    ret = 0
    for dict in list_dict:
        ilosc = 10000
        for letter1 in dict:
            if letter1 not in dict_letters:
                ilosc = 0
                break
            if(dict_letters[letter1] / dict[letter1] < ilosc):
                ilosc = dict_letters[letter1] / dict[letter1]
        if ilosc > ret:
            ret = ilosc
    return ret


def createcaption2(ciag, lista):
    ret = 0
    ilosc = 0
    indeks = 0
    local = ciag
    for nazwa in lista:
        ilosc = 0
        local = ciag
        br = False
        while(True):
            for litera in nazwa:
                if litera not in local:
                    br = True
                    break
                pos = local.find(litera)
                local = local[0:pos] + local[pos+1:]
            if br:
                break
            ilosc+=1
        if ilosc > ret:
            ret = ilosc
    return ret


def test():
    if createcaption1("AAALLLAAABOBBOBKOKOKOKO", ("ALA", "BOB", "KO")) != 4:
        print("błąd 1")
    if createcaption1("TOMTTMMOOLOSSOMOTL", ("TOM", "LOS")) != 4:
        print("błąd 2")
    if createcaption1("OSDGONEOVSKXAJDAAFYUBYEBVSAN", ("ALA", "BOB", "KO")) != 1:
        print("błąd 3")

test()