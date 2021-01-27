from django.shortcuts import render

from scraping.models import Vacancy


def home(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'scraping/home.html', {'vacancies': vacancies})
