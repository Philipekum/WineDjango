from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'WineAnalyzer/home.html')


def about(request):
    articles = Articles.objects.all()
    return render(request, 'WineAnalyzer/about.html', {'articles': articles})


def analyzer(request):
    if request.method == 'POST':
        print('!!!')
        fa = request.POST.get('fixed acidity')
        va = request.POST['volatile acidity']
        ca = request.POST['citric acid']
        rs = request.POST['residual sugar']
        ch = request.POST['chlorides']
        fsd = request.POST['free sulfur dioxide']
        tsd = request.POST['total sulfur dioxide']
        dens = request.POST['density']
        ph = request.POST['pH']
        sulp = request.POST['sulphates']
        alc = request.POST['alcohol']

        result = list(map(float, [fa, va, ca, rs, ch, fsd, tsd, dens, ph, sulp, alc]))

    else:
        result = -1

    return render(request, 'WineAnalyzer/analyzer.html',
                  {'acids': ['fixed acidity', 'volatile acidity', 'citric acid'],
                   'sugar_chlorides': ['residual sugar', 'chlorides'],
                   'sulfur_dioxides': ['free sulfur dioxide', 'total sulfur dioxide'],
                   'others': ['density', 'pH', 'sulphates', 'alcohol'],
                   'result': result})
