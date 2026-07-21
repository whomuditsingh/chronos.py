import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

# Create Sentiment Analyzer object
sia = SentimentIntensityAnalyzer()

# Input text
text = input("Enter a sentence: ")

# Get sentiment scores
scores = sia.polarity_scores(text)

# Display scores
print("\nSentiment Scores:")
print("Positive :", scores['pos'])
print("Negative :", scores['neg'])
print("Neutral  :", scores['neu'])
print("Compound :", scores['compound'])

# Determine overall sentiment
if scores['compound'] >= 0.05:
    print("\nOverall Sentiment: Positive ")
elif scores['compound'] <= -0.05:
    print("\nOverall Sentiment: Negative ")
else:
    print("\nOverall Sentiment: Neutral ")
