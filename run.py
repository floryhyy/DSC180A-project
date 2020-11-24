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

    if 'data' in targets or 'graph' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        # make the data target
        search_terms,texts,authors = get_data(**data_cfg)
        #format data
        content = make_content_all(search_terms,texts,authors)
        sentences = []
        for text in all_text:
            sentences += text_to_sentences(text, tokenizer)
            
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
