text = "This is a sample text. This text contains sample words."
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print("Word Frequencies:", frequency)
