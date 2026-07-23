import nltk
from nltk.corpus import wordnet

# Download WordNet
nltk.download('wordnet')
nltk.download('omw-1.4')

# Input word
word = input("Enter a word: ")

synonyms = set()
antonyms = set()

# Find synonyms and antonyms
for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())

        if lemma.antonyms():
            antonyms.add(lemma.antonyms()[0].name())

# Display results
print("\nSynonyms:")
if synonyms:
    for synonym in sorted(synonyms):
        print(synonym)
else:
    print("No synonyms found.")

print("\nAntonyms:")
if antonyms:
    for antonym in sorted(antonyms):
        print(antonym)
else:
    print("No antonyms found.")
