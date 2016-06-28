#Code Wars: Remove the minimum 7 Kyu
#What : Give an array, remove the smallest values
    #if there are multiple elements of the same values
    #in the array, remove the one with the lower index
    #if you get an empty array return the array empty
    #dont change the order

    #How:
      # Have a list of numbers
      #use min or for loop to compare
      #if numbers == [], return numbers

def remove_smallest(numbers):

    if len(numbers) < 1 :
        print numbers

    else:
        numbers.remove(min(numbers))
        print numbers

remove_smallest([1, 2, 3, 1, 1])
