import pandas as pd
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

