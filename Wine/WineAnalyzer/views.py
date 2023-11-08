from django.shortcuts import render

menu = ["О сайте", "Добавить статью", "Обратная связь"]


def home(request):
    return render(request, 'WineAnalyzer/home.html')
