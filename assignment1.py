"""LING 131A ASSIGNMENT 1

Solve the five problems below. Do this by editing the skeleton code given. Do
not change the names of the functions in the skeleton code. You are free to add
more functions as you see fit. You may use standard Python libraries if you are
aware of them, but all you need to do this assignment has been presented in
class.

The problems are more or less listed in order of increasing difficulty. The
first three are the easiest, 4 is a bit harder and 5 is the trickiest.

Edit this file and then submit it on LATTE. This is due September 16th. Late
submissions are accepted till September 17th 12:30 (beginning of class), but
late submission may trigger a penalty of up to 20%.


PROBLEM 1.

Write a function called is_determiner() that takes a word as input and decides
wheter it is a determiner.

>>> is_determiner('the')
True
>>> is_determiner('thesis')
False

Then create another function remove_determiners() that uses is_determiner() and
that eliminates all determiners in a piece of a text.

>>> remove_determiners('The dog is asleep in a basket.')
'dog is asleep in basket.'

Do not worry about punctuation, but do worry about capitalization, so you want
to remove words like 'The'. You do not need to get all determiners, but you
should go beyond 'the' and 'a' and include possessives and demonstratives. See
https://en.wikipedia.org/wiki/Determiner for some background.


PROBLEM 2.

Write a function called remove_middle1() that removes some interior part of a
list. The function takes three arguments: the list to remove elements from, the
index of the first element to remove, and the index of the last element to
remove.

>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> remove_middle1(lst, 3, 7)
>>> lst
[1, 2, 3, 9]

This is easier than you might think. But do consider what happens when you want
to use the function to remove the third through seventh element of a list that
has only two elements.

Part two of this problem is to write a function remove_middle2() that does the
same, except that it does not change the list that you hand in, instead, it
returns a new list that has the elements removed.

>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> new_lst = remove_middle2(lst, 3, 7)
>>> new_lst
[1, 2, 3, 9]
>>> lst
[1, 2, 3, 4, 5, 6, 7, 8, 9]


PROBLEM 3.

Given a string like the following, return a list of tuples, with each tuple
containing the word token and its length.

>>> get_tokens_and_lengths("Top sites on the Internet")
[('Top', 3), ('sites', 5), ('on', 2), ('the', 3), ('Internet', 8)]


PROBLEM 4.

Write a Python function count_strings() to count the number of strings where the
string length is 3 or more and the first and last character are from a given
sequence of characters. The function takes two arguments, the input list and the
characters to check for.

>>> count_strings(['the', 'cat', 'is', 'asleep'], 'etc')
2

This returns 2 because only "the" and "cat" match the requirements. The others
are too short ("is") or do not start and end with the specified characters
("is" and "asleep").


PROBLEM 5.

Write a function has_most_consonants() that takes a string as input and returns
the words that have the largest number of consonants in them. For this exercise,
consonants are just letters like t and k (in fact, all letters except a, e, i, o
and u). You may use split() to get the tokens and you do not need to worry about
splitting off punctuations.

>>> sorted(has_most_consonants('The door is closed. And many dogs barked.'))
['barked.', 'closed.']
>>> has_most_consonants('')
[]

"""


# PROBLEM 1 - determiners

def is_determiner(word):
    determiners = ['the', 'a', 'an', 'this', 'that', 'those', 'my', 'his', 'her', 'their',
    'some', 'many', 'every', 'few', 'no', 'each', 'any', 'either', 'neither', 'which',
    'what', 'whose']
    return word.lower() in determiners

def remove_determiners(text):
    text_words = text.split()

    for word in text_words:
        if is_determiner(word):
            text_words.remove(word)

    return ' '.join(text_words)


# PROBLEM 2 - remove interior of list

def remove_middle1(lst, first, last):
    temp = lst[0:first]
    temp.extend(lst[last+1:])
    lst[:] = temp
    # A better way to do this would be to use remove_middle2:
    # lst[:] = remove_middle2(lst, first, last)

def remove_middle2(lst, first, last):
    temp = lst[0:first]
    temp.extend(lst[last+1:])
    return temp


# PROBLEM 3 - tokens and their lengths

def get_tokens_and_lengths(text):
    text_words = text.split()
    tokens_and_lengths = []

    for word in text_words:
        tokens_and_lengths.append((word, len(word)))

    return tokens_and_lengths


# PROBLEM 4 - counting strings

def count_strings(lst, chars):
    count = 0
    for word in lst:
        size = len(word)
        if size >= 3 and word[0] in chars and word[size-1] in chars:
            count += 1

    return count


# PROBLEM 5 - consonants

def has_most_consonants(text):
    vowels = ['a','e','i','o','u']
    text_words = text.split()
    final_list = []

    if len(text_words) > 0:
        cons_to_full = {}

        #Takes out all of the vowels for each word
        for word in text_words:
            cons_only = word.lower()
            for vowel in vowels:
                cons_only = cons_only.replace(vowel, '')

            #Adds a dictionary entry from the vowel-less form to the full form
            cons_to_full[cons_only] = word

        #Finds the word with the max number of consonants
        max_cons = len(max(cons_to_full.keys(), key=len))

        #Finds all of the words who have that same max number of consanants

        for key in cons_to_full.keys():
            if len(key) == max_cons:
                final_list.append(cons_to_full[key])

    return final_list


if __name__ == '__main__':

    # Here you can put code where you test what you are doing, for example
    # print(is_determiner("Door"))

    # Or you can use doctest
    import doctest
    doctest.testmod()
