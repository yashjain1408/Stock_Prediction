from symtable import Symbol
from django.shortcuts import render
import pickle as pkl

# Create your views here.

def index(request):
    return render(request, 'index.html')

def load(fileName):
    file = open(fileName, 'rb')
    data = pkl.load(file)
    file.close()
    return data

def predict(request):
    model = load('model.pkl')
    enc = load('label_encoding.pkl')

    Symbol = request.GET['Symbol']
    Date = request.GET['Date']
    Open = int(request.GET['Open'])
    High = int(request.GET['High'])
    Low = int(request.GET['Low'])
    Close = int(request.GET['Close'])
    Adj_close = int(request.GET['Adj_close'])
    Volume = int(request.GET['Volume'])
    Symbol = enc.transform([Symbol])
    test_data = [[Symbol, Open, High, Low, Volume]]
    y_pred = model.predict(test_data)

    return render(request, 'prediction.html' ,{'pred': int(y_pred[0])})
