import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor



#Load the data
#read train.csv and store it in 'X'
X=pd.read_csv('C:\Users\Eliza\.vscode\anorexiav2\Trainingmentalhealth copy.xlsx')
#read test.csv and store it in 'X_test'
X_test=pd.read_csv('')


X.dropna(axis=0,subset=['Prognosis'],inplace=True)
y=X.Prognosis
X.drop(['Prognosis'],axis=1,inplace=True)
print(y)
X_train,X_valid,y_train,y_valid=train_test_split(X,y,train_size=0.8,test_size=0.2)
model=RandomForestRegressor()
model.fit(X_train,y_train)