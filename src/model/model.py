import networkx as nx
from snapy import MinHash, LSH

def build_graph(content, n_permutations, n_gram,out_path):
    lsh = create_lsh(content, n_permutations, n_gram)
    graph = add_similar_edges(lsh,content)
    f = open(out_path, "w")
    f.close()
    for i in opioid_drugs.edges:
        f.write(i+' '+opioid_drugs.edges[i]['author_id']+'\n')
    f.close()

    
def create_lsh(content, n_permutations, n_gram):
    labels = content.keys()
    values = content.values()
    #Create MinHash object
    minhash = MinHash(values, n_gram=n_gram, permutations=n_permutations, hash_bits=64, seed=3)
    
    #Create LSH model
    lsh = LSH(minhash, labels, no_of_bands=5)
    
    return lsh
def add_similar_edges(lsh, content):
    graph=nx.DiGraph()
    #For all items in content
    ls = {}
    for index, text in content.items():
        
        #If item is one of the search terms
        if type(index) == int:
            q = lsh.query(index, min_jaccard=0.2)
            
            #For all matches found
            for match in q:
                
                #If matched item is from the reddit text
                if type(match) != int:
                    author = match.split("_")[0]
                    if author not in ls.keys():
                        ls[author] = [text]
                    else:
                        ls[author].append(text)
    for i in ls:
        ls[i]=list(set(ls[i]))
        total=len(ls[i])
        for n in range(total):
            for j in list(range(total))[n+1:]:
                graph.add_edge(ls[i][n],ls[i][j],author_id=i)
    return graph