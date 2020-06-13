import numpy as np
import pandas as pd
import os
import sys
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import mean_absolute_error
from rdkit.Chem import Descriptors
from rdkit import DataStructs
from rdkit.Chem import MACCSkeys
from rdkit.Chem.AtomPairs import Pairs
from sklearn.model_selection import train_test_split
from rdkit.Chem import Descriptors
from sklearn.decomposition import PCA
from sklearn.svm import SVR
from sklearn.metrics import r2_score
from gensim.models import word2vec
from mol2vec.features import mol2alt_sentence, MolSentence, DfVec, sentences2vec
import csv

if(__name__=='__main__'):
    model = word2vec.Word2Vec.load('/content/300dm/model_300dim.pkl')

    fdf = pd.read_csv('/content/data/22bba507-efcf-4af0-b9d0-f26193605457_train.csv')
    tdf = pd.read_csv('/content/final_test_q3/4b566bb4-3155-49ff-91e1-19942504b20c_test.csv')

    c_tdf = tdf.copy()
    target = fdf['Binding Affinity']
    fdf.drop(columns='Binding Affinity',inplace=True)
    fdf['mol'] = fdf['SMILES sequence'].apply(lambda x: Chem.MolFromSmiles(x))
    fdf['sentence'] = fdf.apply(lambda x: MolSentence(mol2alt_sentence(x['mol'], 1)), axis=1)
    fdf['mol2vec'] = [DfVec(x) for x in sentences2vec(fdf['sentence'], model, unseen='UNK')]
    X = np.array([x.vec for x in fdf['mol2vec']])
    y = target.values

    tdf['mol'] = tdf['SMILES sequence'].apply(lambda x: Chem.MolFromSmiles(x))
    tdf['sentence'] = tdf.apply(lambda x: MolSentence(mol2alt_sentence(x['mol'], 1)), axis=1)
    tdf['mol2vec'] = [DfVec(x) for x in sentences2vec(tdf['sentence'], model, unseen='UNK')]
    x_t = np.array([x.vec for x in tdf['mol2vec']])

    xx_t = np.array(c_tdf)

    fsvr = SVR(kernel = 'rbf',C =100,epsilon=1.5,gamma='scale')
    fsvr.fit(X, y)
    fy_pred = fsvr.predict(x_t)

    filename="submission.csv"
    fields = ['SMILES sequence', 'Binding Affinity']
    rows = []
    for i in range(len(fy_pred)):
        row = []
        row.append(xx_t[i][0])
        row.append(fy_pred[i])
        rows.append(row)
    with open(filename, "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(fields) 
        csvwriter.writerows(rows)