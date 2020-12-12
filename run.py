#!/usr/bin/env python

import sys
import json

sys.path.insert(0, 'src/data')
sys.path.insert(0, 'src/analysis')
sys.path.insert(0, 'src/model')

from data import get_data
from format_data import make_content_text
from format_data import make_content_search
from analysis import get_similar_ls
from model import update_entity_type


def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''
    if 'test' in targets:
        # load short version of data
        text_fp = 'test/textdata'
        term1 = 'test/testdata/terms.csv'
        term2 = 'test/testdata/terms2.csv'
        terms,docs,ontology= get_data(term1,term2,text_fp)

        #format data
        content_ls = make_content_search(terms)
        make_content_text(content_ls,docs)
        
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)
        # make the data target
        similar_ls = get_similar_ls(content_ls, **analysis_cfg)
        
        update_entity_type(docs,similar_ls,terms,ontology, 'test_result.csv')
    
    if 'data' in targets or 'parse_entity' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        # load data
        terms,docs,ontology= get_data(**data_cfg)

        #format data
        content_ls = make_content_search(terms)
        make_content_text(content_ls,docs)
        
    if 'parse_entity' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)
        # get list of matching nouns 
        similar_ls = get_similar_ls(content_ls, **analysis_cfg)

        with open('config/model-params.json') as fh:
            model_cfg = json.load(fh)
        # make the data target
        update_entity_type(docs,similar_ls,terms,ontology, **model_cfg)


if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
