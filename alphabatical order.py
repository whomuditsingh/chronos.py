def sort_sentence_alphabetically(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=str.lower)
    return ' '.join(sorted_words)

input_sentence = "The quick brown fox jumps over the lazy dog"
sorted_sentence = sort_sentence_alphabetically(input_sentence)
print("Sorted sentence:", sorted_sentence)