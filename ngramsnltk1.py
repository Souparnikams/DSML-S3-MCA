from nltk import ngrams
sentence=input("Enter the sentence:")
n=int(input("Enter the value for:"))
n_grams = ngrams(sentence.split(),n)
print("ngramsprinting")
for grams in n_grams:
  print(grams)