from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"welcome.html")

def taxCal(request,number):
    rate = 0.15
    total = number + (number*rate)
    return render(request,"taxCalculation.html",{"total": total, "number": number, "rate": rate})

def display_tax(request,rate):
    return render(request,"displayRate.html",{"rate": float(rate) *100})



