
vowels = ['a','e','i','o','u']

def has_most_consonants(text):
    text_words = text.split()
    cons_to_full = {}
    
    for word in text_words:
        cons_only = word.lower()
        for vowel in vowels:
            cons_only = cons_only.replace(vowel, '')
        cons_to_full[cons_only] = word

    max_cons = len(max(cons_to_full.keys(), key=len))
    final_list = []

    for key in cons_to_full.keys():
        if len(key) == max_cons:
            final_list.append(cons_to_full[key])

    return final_list



p5str = 'The door is closed. And many dogs barked.'
p5 = has_most_consonants(p5str)
print(p5)
