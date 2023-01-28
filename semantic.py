import spacy
nlp = spacy.load('en_core_web_md')

########################################################
## Code 1
########################################################
# 
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

########################################################
## Code 2
########################################################

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

########################################################
## Code 3
########################################################

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

####################################################################
# My thoughts about the similarities between cat, monkey and banana
####################################################################

# I find it interesting that the monkey and banana almost half similar
# Apart from cat and monkey similarity, the cat is mainly is not similar to any given words
# I can see this comparison might have some short-comings.

####################################################################
# Examples of my own
####################################################################

# Code 1 examples:
word1 = nlp("stone")
word2 = nlp("plant")
word3 = nlp("human")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Code 2 examples:
tokens = nlp('stone plant human')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Code 3 examples:
sentence_to_compare = "Why are humans so cruel?"
sentences = ["where did my plant go",
"Hello, this is my special stone",
"I\'ve lost my house in a tornado",
"I\'d like my life back",
"I will name my plant Hector"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


####################################################################
# when used en_core_web_sm instead of en_core_web_md
####################################################################

# I got the below message:
# The model you're using has no word vectors loaded, 
# so the result of the Doc.similarity method will be based on the tagger, 
# parser and NER, which may not give useful similarity judgements. 
# This may happen if you're using one of the small models, e.g. `en_core_web_sm`, 
# which don't ship with word vectors and only use context-sensitive tensors. 
# You can always add your own word vectors, or use one of the larger models instead if available.