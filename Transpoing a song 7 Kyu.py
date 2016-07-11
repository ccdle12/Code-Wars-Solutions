#Code Wars: Transposing a song 7 Kyu
#What : Transposing a song means shifting the value of the note
#given an input song notes and interval, shift each note by the interval according to the structure of notes
    #How:
        #Create list of notes
        #algorithm to match the index of th enote and return it by the interval
        #list ==> for loop to shift by interval ==> string but in list comprehension
        #now just need to change the flats into Sharps
        #list index out range
        #need to figure out
        #if i == notes[-1]:
            #go to notes[0] and continue iterating
        #need to have the difference from Song index to the end of notes then subtract from interval

def transpose(song, interval):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    song = [s.replace('Bb', 'A#') for s in song]
    song = [s.replace('Db', 'C#') for s in song]
    song = [s.replace('Eb', 'D#') for s in song]
    song = [s.replace('Gb', 'F#') for s in song]
    song = [s.replace('Ab', 'G#') for s in song]

    new = list()

    for i in song:

        diff = len(notes) - notes.index(i)

        if notes.index(i) + interval >= len(notes):
            new.append(notes[0 + (interval - diff)])

        else:
            new.append(notes[notes.index(i) + interval])

    print new


transpose(['C', 'C', 'C#', 'D', 'F', 'D', 'F', 'D', 'D', 'C#', 'C', 'G', 'C', 'C'], 11)
