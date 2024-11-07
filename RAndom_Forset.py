#%% RF

import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt 

df = pd.read_csv("C:/Users/akash/titanic.csv")
df.head()

#%%

NAs = pd.concat([df.isnull().sum()], axis = 1, keys = ['Train'])

NAs[NAs.sum(axis = 1)>0]

#%%
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0])

#%%

df['Pclass'] = df['Pclass'].apply(str)
#%%
for col in df.dtypes[df.dtypes == 'object'].index:
    for_dummy = df.pop(col)
    df = pd.concat([df, pd.get_dummies(for_dummy, prefix = col)], axis = 1)
df.head()
#%% 

labels = df.pop("Survived")
#%%
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df, labels, test_size = 0.25)
rf = RandomForestClassifier()

#%%
rf.fit(x_train, y_train)
y_pred = rf.predict(x_test)

#%%

from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(fpr, tpr)
roc_auc
#%%

n_estimators = [1, 2, 4, 8, 16, 32, 64, 100, 200]
train_results = []
test_results = []

for estimator in n_estimators:
    rf = RandomForestClassifier(n_estimators = estimator, n_jobs=-1)
    rf.fit(x_train, y_train)
    df_pred = rf.predict(x_train)
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    roc_auc = auc(fpr, tpr)
    train_results.append(roc_auc)
    y_pred = rf.predict(x_test)
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    roc_auc = auc(fpr, tpr)
    test_results.append(roc_auc)
    
from matplotlib.legend_handler import HandlerLine2D
line1, = plt.plot(n_estimators, train_results, 'b', label = "Train AUC")                                                                                    
line2, = plt.plot(n_estimators, test_results, 'r', label = "Test AUC")
plt.legend(handler_map= {line1: HandlerLine2D(numpoints = 2)})
plt.ylabel("AUC score")
plt.xlabel('n_estimators')
plt.show()















