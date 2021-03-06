# text classification - used to classify a body of text (i.e. inbox mail and spam mail)
# often gives a positive or negative connotation

import nltk
import random
from nltk.corpus import movie_reviews

document = [(list(movie_reviews.words(fileid)), category) 
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]

# train and test with no bais
random.shuffle(document)

all_words = []
for word in movie_reviews.words():
	all_words.append(word.lower())

# perform a frequency distribution
all_words = nltk.FreqDist(all_words)

# set a limit for the number of commonly used words to 3000
word_features = list(all_words.keys())[:3000]

# find the features that we're using
def find_features(document):
	words = set(document)
	features = {}
	for word in word_features:
		features[word] = (word in words)

	return features

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [ (find_features(rev), category) for (rev, category) in document]