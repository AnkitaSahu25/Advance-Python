#Remove duplicate words from a sentence using set.
sentence = "python is easy and python is powerful"
words = sentence.split()

unique_words = set(words)
print(" ".join(unique_words))
