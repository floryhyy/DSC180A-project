import spacy
import os
import ParsedObj
from collections import Counter


class spacy_txt():

    def read_file(self, dir_path):
        e = []
        n = []
        docs = []
        print(sorted(os.listdir(dir_path)))
        for filename in sorted(os.listdir(dir_path)):
            doc = ParsedObj.bare_document()
            file = open(dir_path+"/"+filename, "r",encoding="utf8",errors='ignore')
            Lines = file.readlines()
            i = 0
            for l in Lines:
                sent = ParsedObj.bare_sentence()
                ent, noun, verb = self.process_sent(l)
                n.extend(noun)
                e.extend(ent)
                sent.noun.extend(noun)
                sent.verb.extend(verb)
                sent.ner.extend(ent)
                sent.sentence_id=i
                doc.sentences[i]= sent
                i=i+1
            doc.path=dir_path+"/"+filename
            doc.doc_id=filename
            docs.append(doc)
        return docs, e, n
    def process_sent(self, str_text):
        nlp = spacy.load("en_core_web_sm")
        merge_pipe = nlp.create_pipe("merge_noun_chunks")
        nlp.add_pipe(merge_pipe)
        merge_pipe = nlp.create_pipe("merge_entities")
        nlp.add_pipe(merge_pipe)
        merge_pipe = nlp.create_pipe("merge_subtokens")
        nlp.add_pipe(merge_pipe)
        merge_pipe = nlp.create_pipe("sentencizer")
        nlp.add_pipe(merge_pipe)
        noun = []
        verb = []
        entity = []
        sentence = {}

        doc = nlp(str_text)
        for token in doc:
            if not token.is_stop:
                if token.pos_ in ['PROPN', 'NN', 'NOUN', 'NNP']:
                 print(token.text)
                 noun.append(token.text)
                if token.pos_ in ['VERB']:
                    verb.append(token.text)
        for ent in doc.ents:
            print(ent.text,  ent.label_)
            e = {}
            e[str(ent.text)]=ent.label_
            entity.append(e)

        return entity, noun, verb

    def __init__(self):
        print("gg")



