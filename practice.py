# Set up a letter counter in a string. Count the top 3 most occuring letters and then print the letter and the number of occurances of that letter. Next if the number
# of occurances are the same put them in alphabetical order. 
def counter(name):
    letters = {}
    name = name.lower()
    for letter in name:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
        
    #letters = letters(sorted(name.items, key=lambda item: item[1], reverse=True))
    #top = sorted(letters.items())[:3]
    top = sorted(letters.items(), key=lambda item: (-item[1], item[0]))[:3]

    for key, value in top:
        print(f"{key} {value}")





if __name__ == '__main__':
    value = "aaabbbbeeccc"
    counter(value)