#!/usr/bin/env python

import sys
import json

sys.path.insert(0, 'src/data')
sys.path.insert(0, 'src/analysis')
sys.path.insert(0, 'src/model')

from data import get_data
from format_data import make_content_all
from format_data import text_to_sentences
from analysis import print_score_from_models
from model import build_graph


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
        reddit = 'test/testdata/fake_reddits.json'
        term1 = 'test/testdata/terms.txt'
        term2 = 'test/testdata/terms2.txt'
        search_terms,texts,authors = get_data(term1,term2,reddit)
        search_terms = search_terms[:100]
        #format data
        content = make_content_all(search_terms,texts,authors)
        sentences = []
        for text in texts:
            sentences += text_to_sentences(text)
        
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)
        # make the data target
        lsh,word2vec=print_score_from_models(sentences,content,search_terms, **analysis_cfg)
        
        build_graph(lsh,content, 'test_result.txt')

    if 'data' in targets or 'graph' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        # load data
        search_terms,texts,authors = get_data(**data_cfg)
        search_terms = search_terms
        #format data
        content = make_content_all(search_terms,texts,authors)
        sentences = []
        for text in texts:
            sentences += text_to_sentences(text)
            
    if 'analysis' in targets or 'graph' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)
        # make the data target
        lsh,word2vec=print_score_from_models(sentences,content,search_terms, **analysis_cfg)
        
    if 'graph' in targets:
        with open('config/model-params.json') as fh:
            model_cfg = json.load(fh)
        # make the data target
        build_graph(lsh,content, **model_cfg)


if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
