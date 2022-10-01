def lemmetize_print(words):
     import nltk
     from nltk.stem import WordNetLemmatizer
     from nltk.tokenize import word_tokenize
     lemmatizer = WordNetLemmatizer()
     a = []
     tokens = word_tokenize(words)
     for token in tokens:
          lemmetized_word = lemmatizer.lemmatize(token)
          a.append(lemmetized_word)
     sentence = " ".join(a)
     print(sentence)
     tokens = nltk.word_tokenize(sentence)
     occurrence = {item: tokens.count(item) for item in tokens}
     print(occurrence)


text = input("enter text:")
lemmetize_print(text)


