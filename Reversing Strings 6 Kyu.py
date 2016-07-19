#Reversing String Algorithm 6 Kyu

def spin_words(sentence):

    lst = []

    for i in sentence.split():
        if len(i) >= 5:
            lst.append(''.join(list(i)[::-1]))
        else:
            lst.append(i)

    print ' '.join(lst)

#Best Practice
#return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

spin_words("hey fellow warriors")
