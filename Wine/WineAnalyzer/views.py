from django.shortcuts import render

menu = ["О сайте", "Добавить статью", "Обратная связь"]


def index(request):
    return render(request, 'WineAnalyzer/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'WineAnalyzer/about.html', {'menu': menu, 'title': 'О сайте'})

