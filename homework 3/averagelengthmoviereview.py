import nltk
import pprint
from pprint import *
from nltk.corpus import movie_reviews
from nltk import *

negative_fileids = movie_reviews.fileids('neg')
positive_fileids = movie_reviews.fileids('pos')
#finds average word lenth
tokens1 = movie_reviews.words()
tokenspos = movie_reviews.words(fileids=positive_fileids)
tokensneg = movie_reviews.words(fileids=negative_fileids)
numberlist = [len(w) for w in tokens1]
def Average(lst):
    return sum(lst) / len(lst)

averagelength = Average(numberlist)
print("average lenth of words = ",averagelength)


#conditional distribution of words

searchwords =['good', 'bad', 'amazing', 'awful', 'no', 'not']

  
cfd = ConditionalFreqDist(
    (genre,word)
    for genre in ['pos', 'neg']
    for word in movie_reviews.words(categories=genre)if word in searchwords)
cfd.tabulate()

#for w in searchwords:
 # list1.append((w, tokenspos.count(w)))
#cfTable=ConditionalFreqDist(list1)
#print(cfTable['good'])

print("tokens in pos:",len(tokenspos))
print("tokens in neg:",len(tokensneg))