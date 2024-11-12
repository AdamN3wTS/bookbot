import string
def countCharacterOccurrences(pathh):
    
    book_file = open(f'books/{pathh}')
    book_read = book_file.read()
    book_read = book_read.lower()
    book_file.close()
    letters = [0] *26
    for letter in book_read:
        if letter in string.ascii_lowercase:
            index = string.ascii_lowercase.index(letter)
            letters[index] +=1
    
    tab=[(string.ascii_lowercase[i],letters[i]) for i in range(26)]
    tab.sort(key=lambda x: x[1],reverse=True)
    final = f"--- Begin report of books/frankenstein.txt ---\n{len(book_read)} words found in the document\n"
    
    for letter,count in tab:
        final += f"The '{letter}' character was found {count} times\n"
    final += "--- End report ---"
    return final
    



cco = countCharacterOccurrences('frankenstein.txt')
print(cco)