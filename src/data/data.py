import pandas as pd
def get_data(ontology,mesh_file,reddit_names):
    on=pd.read_csv(ontology,usecols=['opioid1'])
    mesh=pd.read_csv('MESH.csv',usecols=['Preferred Label'])
    mesh_ls = list(set(mesh['Preferred Label']))
    mesh_terms = list(set([i.lower() for i in mesh_ls]))
    on_ls = [i.strip('@en').strip('"') for i in list(set(on['opioid1']))]
    terms = on_ls+mesh_terms
    
    text = reddit_names
    filenames = open(text, 'r').read().split()
    all_text = []
    author_ids = []
    for t in filenames:
        filepath = 'teams/DSC180A_FA20_A00/a07group01/data/' + t + '.json'
        df = pd.read_json(filepath)
        all_text.extend(list(df['text']))
        author_ids.extend(list(df.index))
        
    return terms,all_text,author_ids

