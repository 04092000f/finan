from django.shortcuts import render
import yfinance as yf
import numpy as np
import pandas as pd

def main(request):
    return render(request,'index.html')

def getStock(name):
    stk=yf.Ticker(name)
    his=stk.history(period="0d")
    his=np.array(his.values)
    df = pd.DataFrame(his, columns = ['Open','High','Low','Close','Volume','Dividends','Stock Splits'])
    return df['Open'],df['High'],df['Low'],df['Close'],df['Volume'],df['Dividends'],df['Stock Splits']

def result(request):
    name=str(request.GET['name'])
    o,h,l,c,v,divi,ss=getStock(name)
    o=str(o)
    o=o.lstrip('0')
    o=o.lstrip(' ')
    o=o.rstrip('\nName: Open, dtype: float64')
    o=float(o)
    h=str(h)
    h=h.lstrip('0')
    h=h.lstrip(' ')
    h=h.rstrip('\nName: High, dtype: float64')
    h=float(h)
    l=str(h)
    l=l.lstrip('0')
    l=l.lstrip(' ')
    l=l.rstrip('\nName: Low, dtype: float64')
    l=float(l)
    c=str(c)
    c=c.lstrip('0')
    c=c.lstrip(' ')
    c=c.rstrip('\nName: Close, dtype: float64')
    c=float(c)
    v=str(v)
    v=v.lstrip('0')
    v=v.lstrip(' ')
    v=v.rstrip('\nName: Volume, dtype: float64')
    v=float(v)
    divi=str(divi)
    divi=divi.lstrip('0')
    divi=divi.lstrip(' ')
    divi=divi.rstrip('\nName: Dividends, dtype: float64')
    divi=float(divi)
    ss=str(ss)
    ss=ss.lstrip('0')
    ss=ss.lstrip(' ')
    ss=ss.rstrip('\nName: Stock Splits, dtype: float64')
    ss=float(ss)
    return render(request,'result.html',{'o':o,'h':h,'l':l,'c':c,'v':v,'divi':divi,'ss':ss})
