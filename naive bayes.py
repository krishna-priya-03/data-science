import nltk
from nltk.corpus import movie_reviews
import random


try:
    movie_reviews.categories()
except LookupError:
    nltk.download('movie_reviews')



documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append(
            (movie_reviews.words(fileid), category)
        )



random.shuffle(documents)



all_words = nltk.FreqDist(
    word.lower()
    for word in movie_reviews.words()
)



word_features = list(all_words)[:2000]



def document_features(document):
    document_words = set(document)
    features = {}

    for word in word_features:
        features['contains({})'.format(word)] = (
            word in document_words
        )

    return features



featuresets = [
    (document_features(document), category)
    for (document, category) in documents
]



train_set = featuresets[100:]
test_set = featuresets[:100]



classifier = nltk.NaiveBayesClassifier.train(train_set)



accuracy = nltk.classify.accuracy(
    classifier,
    test_set
)

print("Accuracy:", accuracy)



print("\nMost Informative Features:")
classifier.show_most_informative_features(5)