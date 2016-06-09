#Valid HK number Code Wars 7 Kyu
#What : return boolean True or False if number entered is valid in HK
    #e.g "1234 5678" = True, must have the space inbetween
    #e.g "85648475" = False, no space inbetween
    #only accepts ints
    #if the patter follows int(4 followed by a space and then 4 more its always valid)

    #How:
        #use a re to findall in numbers for a certain pattern?


import re

def is_valid_HK_phone_number(number):
    valid = re.findall("\d*\s\d*$", number)
    return number in valid

def has_valid_HK_phone_number(number):
    hasValid = re.findall("^.*\d{4}\s\d{4}.*$", number)
    return number in hasValid
