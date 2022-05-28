import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split

def ia():

    WIN=pd.read_csv("WIN.csv",sep=",")

    WIN=WIN.reset_index()

    WIN['Target']=WIN['Close'][1:len(WIN)].reset_index(drop=True)

    WIN=WIN.drop('Date',axis=1)

    WIN=WIN.drop(WIN[-1::].index,axis=0)

    WIN=WIN.drop('index',axis=1)

    y=WIN['Target']

    x=WIN.drop(['Target'],axis=1)

    x_treino,x_teste,y_treino,y_teste=train_test_split(x,y,test_size=0.3, shuffle=False)

    modelo=linear_model.LinearRegression()

    modelo.fit(x_treino,y_treino)

    return modelo