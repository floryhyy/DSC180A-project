#!/usr/bin/env python

import sys
import json

sys.path.insert(0, 'src/data')
sys.path.insert(0, 'src/analysis')
sys.path.insert(0, 'src/model')

from data_reddit import get_data
from data_reddit import parse_reddit
from format_data_reddit import make_content_text
from format_data_reddit import make_content_search
from lsh import get_similar_ls
from lsh import update_df
#from emotion import find_lexicon
#from emotion import limbic_score
from dependence import denpendence_parsing
from save_data import save_csv

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''
    if 'test' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        # load short version of data
        folder = 'test/textdata'
        SUBREDDIT="drugs"
        QUERY="test"
        term1 = 'test/testdata/terms.csv'
        term2 = 'test/testdata/terms2.csv'
        terms,ontology,df,QUERY= get_data(term1,term2,folder,SUBREDDIT,QUERY)

        #format data
        dic={QUERY:df}
        content_ls = make_content_search(terms)
        make_content_text(content_ls,dic)
        
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)
        # make the data target
        similar_ls = get_similar_ls(content_ls, **analysis_cfg)
        
        # analysis emotion of sentence
        find_lexicon(df)
        df = limbic_score(df,QUERY)
        #df['is_emotion']=True
        
        #update data
        update_df(similar_ls,df,terms,QUERY)
        
        #parse dependency for identified sentence
        df = denpendence_parsing(df)    
        save_csv(df,'test_data_result.csv')
        
    if 'data' in targets or 'parse_entity' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        # load data
        terms,ontology,df,QUERY= get_data(**data_cfg)
                
        #format data
        dic={QUERY:df}
        content_ls = make_content_search(terms)
        make_content_text(content_ls,dic)

    if 'parse_entity' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)
        # get list of matching nouns 
        similar_ls = get_similar_ls(content_ls, **analysis_cfg)
        
        # analysis emotion of sentence
        find_lexicon(df)
        df = limbic_score(df,QUERY)
        
        #update data
        update_df(similar_ls,df,terms,QUERY)
        
        #parse dependency for identified sentence
        df = denpendence_parsing(df)

        with open('config/model-params.json') as fh:
            model_cfg = json.load(fh)
        # make the data target
        save_csv(df,**model_cfg)


if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
