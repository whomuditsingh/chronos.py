import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams, trigrams

# Download tokenizer
nltk.download('punkt')

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Generate Bigrams
bigram_list = list(bigrams(words))

# Generate Trigrams
trigram_list = list(trigrams(words))

# Display Results
print("\nWords:")
print(words)

print("\nBigrams:")
for bg in bigram_list:
    print(bg)

print("\nTrigrams:")
for tg in trigram_list:
    print(tg)
