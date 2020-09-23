from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'store/index.html')

def about(request):
    return render(request, 'store/about.html')

def clients(request):
    return render(request, 'store/clients.html')

def products(request):
    return render(request, 'store/products.html')

def contact(request):
    return render(request, 'store/contact.html')


def ballbearing(request):
    return render(request, 'store/ballbearing.html')

def strength(request):
    return render(request, 'store/strength.html')

def nut_bolt(request):
    return render(request, 'store/nut_bolt.html')

def hosepipe(request):
    return render(request, 'store/hosepipe.html')

def measuringinstruments(request):
    return render(request, 'store/measuringinstruments.html')

def grindingwheels(request):
    return render(request, 'store/grindingwheels.html')

def circlips(request):
    return render(request, 'store/circlips.html')

def handtools(request):
    return render(request, 'store/handtools.html')