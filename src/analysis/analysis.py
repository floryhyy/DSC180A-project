import pandas as pd
from gensim.models import word2vec
from gensim.models import Phrases
from snapy import MinHash, LSH

def word2vec_model(sentences,mesh_terms,num_feat,num_neighbors):
    model_name = "wv_reddit"
    model = word2vec.Word2Vec(sentences, size=num_feat, window=num_neighbors, min_count=1)
    model.save(model_name)

    #Including bigrams to model
    bigram = Phrases(sentences)
    model = word2vec.Word2Vec(bigram[sentences], min_count=1)

    #Training model on MESH terms
    model.train([mesh_terms], total_examples=1, epochs=1)
    return model

def create_lsh(content, n_permutations, n_gram):
    labels = content.keys()
    values = content.values()
    #Create MinHash object
    minhash = MinHash(values, n_gram=n_gram, permutations=n_permutations, hash_bits=64, seed=3)
    #Create LSH model
    lsh = LSH(minhash, labels, no_of_bands=5)
    return lsh

def print_score_from_models(sentences,content,mesh_terms,num_feat,num_neighbors,n_permutations, n_gram):
    #Going through queries, printing all mapped similar words,
    #and the similarity based on Word2Vec model
    lsh = create_lsh(content, n_permutations, n_gram)
    model = word2vec_model(sentences,mesh_terms,num_feat,num_neighbors)
    for i in content:
        for n in lsh.query(i,min_jaccard=0.2):
            if (type(i)==int) & (type(n)!=int):
                term = content[n].strip('.').strip('?').strip('"')
                if (term in model.wv.vocab) & (content[i] in model.wv.vocab):
                    print(content[i],' ------> ', term)
                    print(model.wv.similarity(content[i], term))
    return lsh,model

