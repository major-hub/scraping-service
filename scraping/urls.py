from django.urls import path

from scraping import views

app_name = 'scraping'

urlpatterns = [
    path('', views.home, name='home'),
]
