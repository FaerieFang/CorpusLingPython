import nltk
sentence = input("enter corpus sentence:")
sentence = str.lower(sentence)
punc = ".!()[]{}:;,?"
for ele in sentence:
    if ele in punc:
        sentence = sentence.replace(ele, "")
tokens = nltk.word_tokenize(sentence)
print(tokens)
occurrence = {item: tokens.count(item) for item in tokens}
print(occurrence)
