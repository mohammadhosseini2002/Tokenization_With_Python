#Sentence Tokenization With nltk Library

import nltk

text = input("enter your text : ")

sentence_tokenization = nltk.sent_tokenize(text)

print("result = " , sentence_tokenization)