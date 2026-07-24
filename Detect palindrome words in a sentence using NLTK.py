import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer
nltk.download('punkt')

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(sentence)

print("\nPalindrome Words:")

found = False

for word in words:
    # Remove non-alphabetic characters
    clean_word = ''.join(char.lower() for char in word if char.isalpha())

    # Check palindrome
    if len(clean_word) > 1 and clean_word == clean_word[::-1]:
        print(clean_word)
        found = True

if not found:
    print("No palindrome words found.")
