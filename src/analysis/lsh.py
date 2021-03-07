from snapy import MinHash, LSH
import re
def create_lsh(content, n_permutations, n_gram):
    labels = content.keys()
    values = content.values()
    #Create MinHash object
    minhash = MinHash(values, n_gram=n_gram, permutations=n_permutations, hash_bits=64, seed=3)
    #Create LSH model
    lsh = LSH(minhash, labels, no_of_bands=5)
    return lsh

def create_lsh_term(content_term,n_permutations, n_gram):
    lsh_ls = {}
    for i in content_term:
        lsh_ls[i] = create_lsh(content_term[i], n_permutations, n_gram)
    return lsh_ls
def update_lsh_text(lsh_ls,content_text,n_permutations, n_gram):
    for i in content_text:
        if i in lsh_ls:
            labels = content_text[i].keys()
            labels = [i+'test' for i in labels]
            values = content_text[i].values()
            minhash = MinHash(values, n_gram=n_gram, permutations=n_permutations, hash_bits=64, seed=3)
            lsh_ls[i].update(minhash,labels)
        else:
            lsh_ls[i] = create_lsh(content_text[i], n_permutations, n_gram)
    return lsh_ls

def get_similar_ls(lsh_ls_term,content_text,n_permutations, n_gram):
    lsh_ls = update_lsh_text(lsh_ls_term,content_text,n_permutations, n_gram)
    edge_list = {}
    for i in lsh_ls:
        edge_list[i] = lsh_ls[i].edge_list(jaccard_weighted=True)
    
    similar_ls = []
    for e in edge_list:
        edges = edge_list[e]
        for i in edges:
            if type(i[1])==int and type(i[0])==str:
                similar_ls.append(i)
            elif (type(i[0])==int and type(i[1])==str):
                similar_ls.append(i)
    return similar_ls
def update_df(ls,df,terms,QUERY):
    term_dic={}
    score_dic={}
    for n in ls:
        word_id = n[0]
        l = len(QUERY+'_post_')
        post_id = int(re.sub('_.+','',word_id[l:]))

        term_id = n[1]
        score = n[2]
        if post_id in term_dic:
            term_dic[post_id].append(terms[term_id])
            score_dic[post_id].append(score)
        else:
            term_dic[post_id] = [terms[term_id]]
            score_dic[post_id]=[score]
    df.loc[list(term_dic.keys()),'matched_drugs'] = list(term_dic.values())
    df.loc[list(score_dic.keys()),'matching_score'] = list(score_dic.values())
