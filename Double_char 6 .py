#CodeWars 7 Kyu

#given a string, return a string where very character is repeated twice

def double_char(s):
    inp = list(s)
    inp2 = []

    for i in inp:
        inp2.append(i*2)
    print ''.join(inp2)


double_char('String')
