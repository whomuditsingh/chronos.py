import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Download required tokenizer
nltk.download('punkt')

# Input paragraph
text = input("Enter a paragraph:\n")

# Convert text to lowercase
text = text.lower()

# Tokenize words
words = word_tokenize(text)

# Remove punctuation
words = [word for word in words if word.isalpha()]

# Calculate word frequency
frequency = FreqDist(words)

print("\nWord Frequency:\n")

for word, count in frequency.items():
    print(f"{word} : {count}")

print("\nMost Frequent Word:")
print(frequency.most_common(1))
