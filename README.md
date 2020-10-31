# Opioid-Use Knowledge Graph Project Template

This repository contains initial code for building a knowledge graph for opioid use in the States. 
The code takes in post from Reddit that including key word about drugs, and generate an association graph for every drug related terms mentioned in the post.
The data.py takes care of input data. analysis.py make a small process on data to make content that can be processed to build graph.
The model.py use lsh search for drug-related terms that mentioned in the post, and build an association graph for terms that appear in the post.

The code can be excuted by python run.py data analysis model



```
### Responsibilities
* Flory developed the majority part of the code,edited LSH part, and formatted code into .py
* Hanbyul developed the LSH part of code and wrote first half of the Introduction
* Gunther got reddit data through API and wrote second half of the Introduction
```

