import pandas as pd
import os
import random
import numpy as np

train_df=pd.read_csv('nCoV_100k_train.labled11.csv')
test_df=pd.read_csv('nCov_10k_test11.csv')
print('error:',train_df[train_df['label']=='-'])
print('error:',train_df[train_df['label']=='·'])
train_df['label']=train_df['label'].fillna(-1)
train_df=train_df[train_df['label']!=-1]
train_df['label']=train_df['label'].astype(int)
#print('error:',train_df[np.logical_and( np.logical_and(train_df['label']!='2',train_df['label']!='1'),\
 #                                       train_df['label']!='0')])
print('error:',train_df[np.logical_and( np.logical_and(train_df['label']!=2,train_df['label']!=1),\
                                        train_df['label']!=0)])
del train_df['time']
del train_df['video']
del train_df['img']
test_df['label']=0
test_df['content']=test_df['content'].fillna('无')
del test_df['time']
del test_df['video']
del test_df['img']
train_df['content']=train_df['content'].fillna('无')
test_df['title']=test_df['title'].fillna('无')
train_df['title']=train_df['title'].fillna('无')

index=set(range(train_df.shape[0]))
K_fold=[]
for i in range(5):
    if i == 4:
        tmp=index
    else:
        tmp=random.sample(index,int(1.0/5*train_df.shape[0]))
    index=index-set(tmp)
    print("Number:",len(tmp))
    K_fold.append(tmp)
    

for i in range(5):
    print("Fold",i)
    os.system("mkdir data_{}".format(i))
    dev_index=list(K_fold[i])
    train_index=[]
    for j in range(5):
        if j!=i:
            train_index+=K_fold[j]
    train_df.iloc[train_index].to_csv("data_{}/train.csv".format(i))
    train_df.iloc[dev_index].to_csv("data_{}/dev.csv".format(i))
    test_df.to_csv("data_{}/test.csv".format(i))
