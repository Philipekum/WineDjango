import random
from django.shortcuts import render
from .backup import combine_to_df_and_predict
from .forms import *
from .models import *


def home(request):
    return render(request, 'WineAnalyzer/home.html')


def about(request):
    articles = Articles.objects.all()
    return render(request, 'WineAnalyzer/about.html', {'articles': articles})


def analyzer(request):
    if request.method == 'POST':
        response = request.POST

        form = ElementsInput(response)

        random_change = random.randint(-2, 2)

        result = combine_to_df_and_predict(response)[0] + random_change



    else:
        form = ElementsInput()

        result = -1

    return render(request, 'WineAnalyzer/analyzer.html', {'form': form,
                                                          'result': result,
                                                          'stars': list(range(1, 11))})
