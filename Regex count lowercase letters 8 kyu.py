#CodeWars Regex count lowercase letters 8 Kyu
#What : count the total number of lowercase letters in a string
    #How:
        #Enter strng
        #import re
        #findall in strng/ put into list/ count length
        #print

#best practice
def lowercase_count(strng):
    import re
    return len(re.findall('[a-z]', strng))
