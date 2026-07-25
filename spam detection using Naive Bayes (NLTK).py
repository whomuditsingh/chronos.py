import nltk
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier

# Download required tokenizer
nltk.download('punkt')

# Sample training dataset (it can be trained with more data for optimizing this code)
training_data = [
    ("Congratulations! You have won a lottery prize.", "Spam"),
    ("Claim your free gift now.", "Spam"),
    ("You have been selected for a cash reward.", "Spam"),
    ("Limited time offer! Buy now.", "Spam"),
    ("Win a free vacation today.", "Spam"),

    ("How are you doing today?", "Ham"),
    ("Let's meet for lunch tomorrow.", "Ham"),
    ("Please submit your assignment by Monday.", "Ham"),
    ("Happy Birthday! Have a great day.", "Ham"),
    ("Can you call me when you are free?", "Ham")
]

# Feature extraction function
def extract_features(text):
    words = word_tokenize(text.lower())
    return {word: True for word in words}

# Prepare training set
train_set = [(extract_features(text), label) for text, label in training_data]

# Train Naive Bayes Classifier
classifier = NaiveBayesClassifier.train(train_set)

# Input message
message = input("Enter a message: ")

# Predict
result = classifier.classify(extract_features(message))

print("\nPrediction:", result)

# Show probability distribution
prob = classifier.prob_classify(extract_features(message))

print("\nProbability:")
print("Spam :", round(prob.prob("Spam"), 2))
print("Ham  :", round(prob.prob("Ham"), 2))
