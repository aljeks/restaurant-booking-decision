#!/usr/bin/env python
# coding: utf-8

import pickle

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.metrics import mutual_info_score
from sklearn.model_selection import train_test_split, GridSearchCV, RepeatedStratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,roc_auc_score 
from sklearn.metrics import auc
import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing

# data preparation

warnings.filterwarnings("ignore")
datafile = 'zomato.csv'
df = pd.read_csv(datafile)
df.columns = df.columns.str.lower().str.replace(' ', '_')
strings = list(df.dtypes[df.dtypes == 'object'].index)
for col in strings:
    df[col] = df[col].str.lower()
columns = ['restaurant_name','city','currency','rating_text','locality','cuisines']
for c in columns:
    df[c] = df[c].str.replace(' ', '_')
for c in columns:
    df[c] = df[c].str.replace(',_', ',')
del df['locality_verbose']
del df['address']
del df['locality']
del df['restaurant_id']
del df['rating_color']
del df['rating_text']
del df['switch_to_order_menu']

df.cuisines = df.cuisines.fillna('NA')
df = df.drop(df[df.average_cost_for_two > 3000].index)

book_decision = (df.aggregate_rating >= 4.2)
df['book_decision'] = book_decision.astype(int)
del df['aggregate_rating']

# Splitting data as Train (60%), Val (20%), Test (20%)
df_full_train, df_test = train_test_split(df,test_size=0.2,shuffle=True,random_state=1)
df_train, df_val = train_test_split(df_full_train,test_size=0.25,shuffle=True,random_state=1)

y_train = df_train['book_decision'].values
y_val = df_val['book_decision'].values
y_test = df_test['book_decision'].values

del df_train['book_decision']
del df_val['book_decision']
del df_test['book_decision']

df_full_train = df_full_train.reset_index(drop=True)
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

train_dicts = df_train.to_dict(orient='records')
val_dicts = df_val.to_dict(orient='records')

dv = DictVectorizer(sparse=False)

X_train = dv.fit_transform(train_dicts)
X_val = dv.transform(val_dicts)

from sklearn.ensemble import RandomForestClassifier

fr = RandomForestClassifier(n_estimators=100, max_depth=13, min_samples_split=2,
                           random_state=42, n_jobs=-1)
fr.fit(X_train, y_train)
y_pred = fr.predict(X_val)
roc_rf = roc_auc_score(y_val, y_pred)
print(f"Roc auc score : {roc_rf}")

model_file = 'model2.bin'
dv_file = 'dv2.bin'

with open(model_file, 'wb') as f_out: 
    pickle.dump((fr), f_out)

with open(dv_file, 'wb') as f_out: 
    pickle.dump((dv), f_out)

print(f'the model is saved to {model_file}')
