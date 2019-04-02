# Natural-Language-Processing-to-Mine-Text-Data
This project explores the options available for creating the frequency form of the term document matrix. This is a matrix or table where each row represents a term in the corpus, the collection of documents, and each column represents a different document. The entries in the matrix is the counts or frequency of each term in each document. There are several options available in constructing this matrix, but three most important and the once which would be focused in this code are: 
1. POS - Parts of Speech 
2. Stop Word Removal 
3. Stemming 
Parts of speech, can be involved, but doing so will take more processing time and may not add that much information to the analysis. Stop word removal is normally done to reduce the number of words that contain little information. These are mostly words that are common to most documents. The last option is whether or not to stem words to their root forms. This too can take additional processing time, but it should reduce the number of unique terms in the term-document matrix. This code evaluates four common scenarios: 
1. POS(Yes) Stop(Yes) Stem(Yes) 
2. POS(Yes) Stop(No) Stem(No) 
3. POS(Yes) Stop(No) Stem(No) 
4. POS(No) Stop(No) Stem(No)