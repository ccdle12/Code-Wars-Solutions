#Count by X codewars 8 kyu

#What: Create a function that takes two arguments and returns a list of of multiples of x in the list length of n
    #How:
        #create function (x,n)
        #x == multiple
        #n == len/range
        #lst = 0

        #for i in range(n):
            #lst = lst + x


def count_by(x, n):

    #num = 0
    #lst = []
    #for i in range(n):
        #num = num + x
        #lst.append(num)
    #return lst
    
    return ([i*x for i in range(n+1) if i != 0])
   

'''
#best practice

return range(x, x * n + 1, x)

