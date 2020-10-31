import pandas as pd
def get_data(reddit,ontology,mesh_file):
    df1=pd.read_json(reddit)
    on=pd.read_csv(ontology,usecols=['opioid1'])
    mesh=pd.read_csv(mesh_file,usecols=['Preferred Label'])
    mesh_ls = list(set(mesh['Preferred Label']))
    on_ls = [i.strip('@en').strip('"') for i in list(set(on['opioid1']))]
    terms = on_ls+mesh_ls
    #extract meds term from reddit file
    def extract(s):
        return re.findall('\d-[A-Z]+[a-z]*[A-Z]+',s)
    ls = df1['text'].apply(extract)
    ls = ls[ls.apply(lambda x: len(x)>0 )]
    for i in ls:
        terms+=list(set(i))
        
    return terms,df1

