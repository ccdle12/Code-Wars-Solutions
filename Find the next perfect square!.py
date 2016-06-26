#Code Wars Find the Next perfect square
  #WHat: find the next integral perfect square after input
    #return -1 if input isn't perfect square

import math # 1 constant

def find_next_square(sq):

    if (math.sqrt(sq)).is_integer() :
    # if (sq/2).is_integer():
         print int(math.sqrt(sq) + 1) **  2
    else:
        print -1

find_next_square(9)
