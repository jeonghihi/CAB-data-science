# code crumbs

# write a method that takes an array of consecutive (increasing) letters 
# as input and that returns the missing letter in the array.

def count_letters(word, char):
    count = 0
    for c in word:
        count += (char == c)
    return count

def count_substring(string, sub_string):
    count = 0
    for pos in range(len(string)):
        if string[pos:].startswith(sub_string):
            count += 1
    return count