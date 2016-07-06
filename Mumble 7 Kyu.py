#Code Wars 7 Kyu - Mumble
#e.g. accum("abcd") --> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") --> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") --> "C-Ww-Aaa-Tttt"

#What: Return string,
    #for i in range(len(s)):
        #print i *

def accum(s):

    lst = []

    m = 1

    for i in s:
        lst.append(i*m)
        m+=1

    #
    print '-'.join(lst).title()

accum("abcd")
