from django.shortcuts import render


def home(request):
    return render(request, 'Market_/home.html')
