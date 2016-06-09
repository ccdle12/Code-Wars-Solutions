#Code Wars: Jaden Case Strings 7 Kyuu
#What: capitalize every word in a string, return the string
    #How:
        #Input string
        #split string into lists
        #string.upper()?
        #convert back to string
        #return

def toJadenCase(a):
    import string
    return string.capwords(a)
