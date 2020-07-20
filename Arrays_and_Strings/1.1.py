def unique_word(word):
    letter_map = {}
    for l in word:
        if( l in letter_map): return "Not Unique"
        else: letter_map[l] = True
    
    return "Unique"

word = input()

print(unique_word(word))

