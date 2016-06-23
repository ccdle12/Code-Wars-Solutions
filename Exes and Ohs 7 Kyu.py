#Code Wars Exes and Ohs 7 Kyu
  # Return boolean True if same amount of "X's" and "O's", if different amount return false
    #Else return error string does not have X's and O'x
    #if there is no X's or O's return True

def xo(s):

    o = s.lower().count('o')
    x = s.lower().count('x')

    if o == x : print True
    elif o != x : print False
    else:
        print True

#Best Practice from website
# def xo(s):
#     return s.lower().count('x') == s.lower().count('o')

#Rough logical sketch
    # countO = 0
    # countX = 0

    # for i in s:
    #     if i == 'o' or i == 'O':
    #         countO += 1
    #     elif i == 'x' or i == 'X':
    #         countX += 1
    #
    # if countO == countX : print True
    # elif countO != countX: print False
    # else:
    #     print True
    # print 'countO:', countO, '  countX:', countX

xo('zzll')
