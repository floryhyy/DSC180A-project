# Opioid-Use Knowledge Graph Project Template

This repository contains initial code for building a knowledge graph for opioid use in the States. 
The code takes in press-release from DEA(Drug Enforcement Administration), or other text file with similar structual and ontology list(RxNorm and Mesh). 
The extracted entity from textual data and get entity type basied on ontology list

The data.py takes care of loading data and formating data
The analysis.py conduct the similar matching to extract entity types based on ontology lisit
The model.py procude a report of matching result

The code can be excuted by 
    - python run.py test 
    - python run.py data 
    - python run.py parse_entity

Target explainnation 
    0: test: test the whole process of code
    1: data： read in, text, and ontology data. And process them into format (e.g.parse nouns from text and put into a dictionary with ontology terms) that can be used for following analysis steps.
    2: parse_entity: use similar matching to extract type for entity(nouns) based on ontology dictionary, and store all the matching entity into output csv files. 


```
### Responsibilities
* Flory developed the code,and formatted code into .py
* Hanbyul helped with LSH part of code and wrote parts of the report
* Gunther got reddit data through API and wrote parts of the report
```

