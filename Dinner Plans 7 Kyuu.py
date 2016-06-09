#Code Wars:
#What: Compare two strings in funciton
#Return all the strings that appear
#How:
    #Compare the strings
    #Iterate to see if they are the same
    #split into list
    #iterate over the list
    #return matching data as a strings
    #if fales return death

#FIND OUT how to not get duplicates in s3 list

from collections import OrderedDict
#OrderedDict removes duplicates but keeps the order
def common_ground(s1, s2):
    s3 = []
    [s3.append(i) for i in s2.split() if i in s1.split()]
    # print s3
    print ' '.join(OrderedDict.fromkeys(s3))

common_ground("aa bb cc", "bb cc bb aa")
