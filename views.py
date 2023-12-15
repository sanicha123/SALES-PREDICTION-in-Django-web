# sales_prediction
import pandas as pd
from django.shortcuts import render 
from django.shortcuts import HttpResponse
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def index(request):
    return render(request, 'home.html')

def userinput(request):
    return render(request, 'userinput.html')

def viewdata(request):
    tv_value = request.GET.get('TV')
    radio_value = request.GET.get('Radio')
    newspaper_value = request.GET.get('Newspaper')

    # Check if any of the values are None
    if tv_value is None or radio_value is None or newspaper_value is None:
        return HttpResponse('Missing one or more input values')

    try:
        # Convert the values to integers (optional, depending on your needs)
        tv_value = int(tv_value)
        radio_value = int(radio_value)
        newspaper_value = int(newspaper_value)
    except ValueError:
        return HttpResponse('Invalid input values. Please enter valid numbers.')

    df = pd.read_csv('C:/Users/Super/Documents/SALES PREDICTION/advertising.csv')
    X = df[['TV', 'Radio', 'Newspaper']]
    y = df['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    data = [tv_value, radio_value, newspaper_value]
    y_pred = lr.predict([data])

    dic = {'pred': y_pred[0]}
    return render(request, 'viewdata.html', dic)
