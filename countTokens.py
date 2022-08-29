import nltk
sentence = input("enter corpus sentence:")
tokens = nltk.word_tokenize(sentence)
print(tokens)
occurrence = {item: tokens.count(item) for item in tokens}
print(occurrence)
