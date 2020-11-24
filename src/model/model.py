import networkx as nx
from snapy import MinHash, LSH

def build_graph(lsh,content,out_path):
    graph = add_similar_edges(lsh,content)
    f = open(out_path, "w")
    f.close()
    for i in graph.edges:
        f.write(i+' '+graph.edges[i]['author_id']+'\n')
    f.close()
    
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