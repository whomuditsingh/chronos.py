import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

# Download required NLTK resources 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(sentence)

# Perform POS tagging
tagged_words = pos_tag(words)

# Perform Named Entity Recognition
named_entities = ne_chunk(tagged_words)

print("\nNamed Entity Recognition (NER):\n")
print(named_entities)

# Display extracted named entities
print("\nExtracted Named Entities:")
for chunk in named_entities:
    if hasattr(chunk, 'label'):
        entity = " ".join(c[0] for c in chunk)
        print(f"{entity} --> {chunk.label()}")
