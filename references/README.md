# Opioid-Use Knowledge Graph Project Template

This repository contains initial code for building a knowledge graph for opioid use in the States. 
The code takes in reddit post that are discussing drugs and ontology list(RxNorm and Mesh),used to extract drug names. 
The emotion in reddit post will be analyzed and the relationship between emotional term and drugs will be established.

The data.py takes care of loading data and formating data
The analysis.py conduct the similar matching to extract drug terms.
The emotion.py will analyze emotion in the reddit post
The dependence.py will perform dependency parsing for sentences that have emotion and drug terms
The model.py procude a report of matching result

The code can be excuted by 
    - python run.py test 
    - python run.py data 
    - python run.py parse_entity

Target explainnation 
    0: test: test the whole process of code
    1: data： read in, text, and ontology data. And process them into format (e.g.parse nouns from text and put into a dictionary with ontology terms) that can be used for following analysis steps.
    2: parse_entity: use similar matching to extract drug terms and perform emotion analysis and dependency parsing, and store result into output csv files. 


```
### Responsibilities
* Flory developed the code,and formatted code into .py
* Hanbyul wrote parts of the report
* Gunther got reddit data through API and wrote parts of the report
```

