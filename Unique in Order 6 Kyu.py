#CodeWars
#What: take the arguments from unique_in_order function
#return a list of items, without any duplicate elements, in the original order of elements
#POP removes the index inp[m] will remove the corresponding character ot the index
#e.g. lst = [a, b, a]
# list.remove(lst[2]) will remove the first appearance of a = lst = [b,a]
#lst.pop(m) = m == 2 // lst == [a,b]
def unique_in_order(iterable):
    inp = list(iterable)
    n = 0
    m = 1

    for i in inp[:-1]:
         if inp[n] == inp[m]:
             inp.pop(m)
         else:
             n+=1
             m+=1
    print inp


unique_in_order('AAAABBBCCDAABBB')
