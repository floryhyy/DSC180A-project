import nltk
import nltk.data
import pandas as pd
import re
def make_content_all(search_terms, text, authors):
    #Initialize a dictionary
    content = dict()
    
    #Add search terms to dictionary with numbered key
    for i in range(len(search_terms)):
        if len(search_terms[i]) > 3:
            content[i] = search_terms[i].strip().lower()
                
    #Add text to dictionary with author as key
    for i in range(len(text)):
        key_n = 0
        for sentence in text[i].split():
            s=sentence.replace(',',' ').strip().lower()
            if len(s) > 5:
                key = authors[i] + "_" + str(key_n)
                content[key] = s
                key_n += 1
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


