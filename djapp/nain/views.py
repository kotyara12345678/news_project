from django.shortcuts import render

def index(request):
    return render(request, 'nain/index.html')

def about(request):
    return render(request, 'nain/about.html')

def help(request):
    return render(request, 'nain/help.html')