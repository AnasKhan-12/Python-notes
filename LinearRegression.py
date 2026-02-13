import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class LinearRegression2:
    def __init__(self):
        self.m=None
        self.b=None

    def fit(self,X_train,y_train):
        num=0
        den=0

        for i in range (X_train.shape[0]):
            num+= (X_train[i] -X_train.mean()) *(y_train[i] - y_train.mean())
            den+= (X_train[i]-X_train.mean())*(X_train[i]-X_train.mean())
        
        self.m=num/den
        self.b=y_train.mean() - (self.m*X_train.mean())
        print(self.m)
        print(self.b)

    def predict(self,X_test):
        
        # print(X_test)
        
        return self.m * X_test + self.b

# abc=LinearRegression()
df=pd.read_csv("placement.csv")
X=df.iloc[:,0].values.reshape(-1,1)
y=df.iloc[:,1].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)
lr=LinearRegression2()
lr.fit(X_train,y_train)
a=lr.predict(X_test)
# abc.fit(X_train,y_train)
# a=abc.predict(X_test)
# print(abc.coef_,abc.intercept_)
print(a)

     

