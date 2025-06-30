def count_vowel_words(s):
    return sum(1 for word in s.lower().split() if word[0] in 'aeiou')
print(count_vowel_words("An elephant is outside")) 
