#6 Kyu - sum of numbers
#return all the sum of all numbers within the range given

def get_sum(a,b):


    if a < b:
        print sum([i for i in range(a, b+1)])
    else:
        print sum([i for i in range(b, a+1)])

get_sum(0, -1)
