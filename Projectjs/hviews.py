from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def home(request):
    return render(request, 'home.html')
def heartpredict(request):
    return render(request, 'heartpredict.html')
def result(request):
    heart_data = pd.read_csv(r"E:\django_pro\Projectjs\heart.csv") 
   
    
    heart_data.head()
    heart_data.tail()
    heart_data.shape
    heart_data.isnull().sum()
    heart_data.describe()
    heart_data['target'].value_counts()
    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target'] 

    print(X)
    print(Y)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
    print(X.shape, X_train.shape, X_test.shape)
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])
    val13 = float(request.GET['n13'])


    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13]])

    result1= ""
    if pred==[1]:
        result1="The Person Does't Have Heart Diseases."
    else:
        result1="The Person Have Heart Disease Takecare Yourselves."



    return render(request, "heartpredict.html", {"result2":result1})