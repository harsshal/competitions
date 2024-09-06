# https://www.hackerrank.com/challenges/predicting-house-prices/problem

from sklearn.linear_model import LinearRegression
import pandas as pd

  
f,n= map(int, input().split())


houses=[]
for i in range(n):
    houses.append(list(map(float,input().split())))

t=int(input())
test=[]
for j in range(t):
    test.append(list(map(float, input().split())))

x_train=[]
y_train=[]
for i in houses:
    x_train.append(i[:-1])
    y_train.append(i[-1])

model=LinearRegression()  
x_trains=pd.DataFrame(x_train)

model.fit(x_trains,y_train)
tests=pd.DataFrame(test)
predicts=model.predict(tests)
for a in predicts:
    print(round(a,2))