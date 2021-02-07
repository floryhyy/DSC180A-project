import pandas as pd
from parse_text import spacy_txt
import json
from nltk.stem import PorterStemmer
import nltk
from nltk.tokenize import word_tokenize


def get_data(rxnorm_fp,mesh_fp,folder,SUBREDDIT,QUERY):
    #read in ontology list
    
    rx=pd.read_csv(rxnorm_fp,usecols=['Preferred Label','Semantic type UMLS property'])
    mesh=pd.read_csv(mesh_fp,usecols=['Preferred Label','Semantic type UMLS property'])
    term = pd.concat([rx,mesh])
    term['Preferred Label'] = term['Preferred Label'].str.lower()
    term['Preferred Label'] = term['Preferred Label'].apply(lambda i :i.strip('(+)-').strip('(),.-{').strip().replace("'",'').replace("}",''))
    ontology = dict(zip(term['Preferred Label'],term['Semantic type UMLS property']))
    terms = list(ontology.keys())
    terms = sorted(terms)
    df = parse_reddit(folder,SUBREDDIT,QUERY)
    return terms,ontology,df,QUERY
def parse_reddit(folder,SUBREDDIT,QUERY):
    TIME = 'year'
    with open(folder+'/'+SUBREDDIT + '_' + QUERY + '_' + TIME + '.json', 'r') as outfile:
        data = json.load(outfile)
    user=[]
    content_type=[]
    text=[]
    def get_replies(comment):
        if len(comment['replies']) > 0:
            for n in comment['replies']:
                c = comment['replies'][n]
                user.append(n)
                content_type.append('reply')
                text.append(c['body'])
                get_replies(c)
        else:
            return

    for i in data:
        content = data[i]
        user.append(i)
        content_type.append('post')
        text.append(content['text'])
        comment = content['comments']
        if len(comment)>0:
            for c in comment:
                comments = comment[c]
                user.append(c)
                content_type.append('comment')
                text.append(comments['body'])
                get_replies(comments)
    df=pd.DataFrame({'user':user,'content_type':content_type,'text':text})
    def clean_text(i):
        tokens = [word.strip() for word in nltk.word_tokenize(i)]
        stemmer = PorterStemmer()
        stems = [stemmer.stem(item) for item in tokens]
        return stems
    df['clean_words'] = df['text'].apply(clean_text)
    df['clean_text'] = df['clean_words'].apply(lambda x : ' '.join(x))
    df.to_csv('parsed_reddit/'+QUERY+'_reddits.csv',index=False)
    return df


