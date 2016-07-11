#CodeWars: Permutation Average 7 Kyu
#What: Take a number input, rearrange the order for all possible orders and return the average of all the permutation


from itertools import permutations

def permutation_average(n):
    perms = [float(''.join(e)) for e in permutations(str(n))]
    return int(round(sum(perms) / len(perms)))







