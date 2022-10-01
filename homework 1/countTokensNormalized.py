import pprint
import nltk
with open('data.txt', 'r') as file:
    data = file.read().replace('\n', '')
sentence = data
sentence = str.lower(sentence)
punc = ".!()[]{}:;,?"
for ele in sentence:
    if ele in punc:
        sentence = sentence.replace(ele, "")
tokens = nltk.word_tokenize(sentence)

occurrence = {item: tokens.count(item) for item in tokens}
sortedTokens = sorted(occurrence.items(), key = lambda x: x[1], reverse = True)
pprint.pprint(sortedTokens)
