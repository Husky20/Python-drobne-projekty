'''
1. Usunięcie 5 - Remove5.py
    a. Z podanej liczby (int) należy usunąć jedną cyfrę „5” tak aby zwrócić maksymalny wynik
    b. Zwrócona wartość musi być w formacie „int”
    c. Przykładowe wejście „-1585” musi generować wyjście „-158” a przykładowe wejście „5835” musi generować wyjście „835”
'''

def remove5(number):
    number = str(number)
    number_of_5 = number.find('5')
    n = []
    for it in range(len(number)):
        if number[it] == '5':
            new_number = number[0:it] + number[it+1:len(number)]
            n.append(int(new_number))
    return max(n)
print(remove5(int(-51853974)))