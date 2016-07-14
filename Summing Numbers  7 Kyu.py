#Codewars 7 Kyu - Summing a numbers digits


def sumDigits(number):


    number = list(str(number))

    if '-' in number:
        number.remove('-')
    #
    n = []
    [n.append(int(i)) for i in number]
    #
    print sum(n)


sumDigits(34243)
