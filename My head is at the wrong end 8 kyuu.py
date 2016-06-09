#CodeWars: My head is a the wrong end
#What: Switch the order of the arrays (tail,body,head) to (head,body,tail)


def fix_the_meerkat(arr):
    return [x for x in reversed(arr)]

#Best Practice:
    #def fix the meerket(arr):
        #return arr[::-1]
