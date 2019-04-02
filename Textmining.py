# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 01:04:30 2019

@author: aashu
"""
#Importing Libraries and Calling Functions
import string
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.probability import FreqDist
from collections import Counter
import operator

#Attaching the file
file_path = '../Text/TextFiles/'
files = ['T1.txt', 'T2.txt', 'T3.txt', 'T4.txt', 'T5.txt', 'T6.txt', \
'T7.txt', 'T8.txt']
term_doc = []
pos_tags = True
stemming = True
remove_stop = True

#Loop to read file
for file in files:
with open (file_path+file, "r") as text_file:
adoc = text_file.read()

#Data Preprocessing and Tokenization
# Convert to all lower case - required
adoc = ("%s" %adoc).lower()
# Replace special characters with spaces
adoc = adoc.replace('-', ' ')
adoc = adoc.replace('_', ' ')
adoc = adoc.replace(',', ' ')
# Replace not contraction with not
adoc = adoc.replace("'nt", " not")
adoc = adoc.replace("n't", " not")
adoc = adoc.replace("'d", " ")
# Tokenize
tokens = word_tokenize(adoc)
tokens = [word.replace(',', '') for word in tokens]
tokens = [word for word in tokens if ('*' not in word) and \
word != "''" and word !="``"]
for word in tokens:
word = re.sub(r'[^\w\d\s]+','',word)
print("\nDocument "+file+" contains a total of", len(tokens), " terms.")

#POS tagging
if pos_tags:
# POS Tagging
tokens = nltk.pos_tag(tokens)

#Stop word removal
if remove_stop:
# Remove stop words
stop = stopwords.words('english') + list(string.punctuation)
stop.append("said")
# Remove single character words and simple punctuation
tokens = [word for word in tokens if len(word) > 1]
# Remove stop words
if pos_tags:
tokens = [word for word in tokens if word[0] not in stop]
tokens = [word for word in tokens \
if (not word[0].replace('.','',1).isnumeric()) and \
word[0]!="'s" ]
else:
tokens = [word for word in tokens if word not in stop]
tokens = [word for word in tokens if word != "'s" ]

#Stemming
if stemming:
# Lemmatization - Stemming with POS
3
# WordNet Lematization Stems using POS
stemmer = SnowballStemmer("english")
wn_tags = {'N':wn.NOUN, 'J':wn.ADJ, 'V':wn.VERB, 'R':wn.ADV}
wnl = WordNetLemmatizer()
stemmed_tokens = []
if pos_tags:
for token in tokens:
term = token[0]
pos = token[1]
pos = pos[0]
try:
pos = wn_tags[pos]
stemmed_tokens.append(wnl.lemmatize(term, pos=pos))
except:
stemmed_tokens.append(stemmer.stem(term))
else:
for token in tokens:
stemmed_tokens.append(stemmer.stem(token))
if stemming:
print("Document "+file+" contains", len(stemmed_tokens), \
"terms after stemming.\n")
tokens = stemmed_tokens

# Prepare counts and addint to term_doc
#fdist = FreqDist(word for word in stemmed_tokens)
fdist = FreqDist(tokens)
# Use with Wordnet
td= {}
#term_doc = []
for word, freq in fdist.most_common(2000):
td[word] = freq
term_doc.append(td)

#Prepering term document matrix
 td_mat = {}
for td in term_doc:
td_mat = Counter(td_mat)+Counter(td)
td_matrix = {}
for k, v in td_mat.items():
td_matrix[k] = [v]
4
for td in term_doc:
for k, v in td_matrix.items():
if k in td:
td_matrix[k].append(td[k])
else:
td_matrix[k].append(0)

#Printing Term Document matrix
td_matrix_sorted = sorted(td_matrix.items(), key=operator.itemgetter(1),\
reverse=True)
print("Scenario: POS=", pos_tags, "Remove Stop Words=", remove_stop, \
" Stemming=", stemming)
print("------------------------------------------------------------")
print(" TERM TOTAL D1 D2 D3 D4 D5 D6 D7 D8")
for i in range(20):
s = '{:<15s}'.format(td_matrix_sorted[i][0])
v = td_matrix_sorted[i][1]
print(v)
for j in range(9):
s = s + '{:>5d}'.format(v[j])
print('{:<60s}'.format(s))
print("____________________________________________________________")