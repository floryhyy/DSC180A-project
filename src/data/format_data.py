import nltk
import nltk.data
import pandas as pd
import re
def make_content(search_terms, text_df, textcol_name):
    #Initialize a dictionary
    content = dict()

    #Add search terms to dictionary with numbered key
    for i in range(len(search_terms)):
        if len(search_terms[i]) > 3:
            content[i] = search_terms[i]

    min_length = min(map(len, search_terms))

    #Add text to dictionary with author as key
    for index, row in text_df.iterrows():
        key_n = 0
        for sentence in row[textcol_name].split('\n'):
            if len(sentence) > 3:
                key = index + "_" + str(key_n)
                content[key] = sentence.strip('\s+').replace(',',' ').lower()
                key_n += 1
            #elif len(sentence.split())>1: 
             #   print(len(sentence),sentence)
    return content

def text_to_list (text):
    cleaned_text = re.sub("[^a-zA-Z]", " ", text)
    words = cleaned_text.lower().split()
    
    return words

def text_to_sentences (text):
    tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
    raw_sentences = tokenizer.tokenize(text.strip())

    sentences=[]
    for s in raw_sentences:
        if len(s) > 0:
            sentences.append(text_to_list(s))
    return sentences


