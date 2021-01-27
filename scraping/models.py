
from django.db import models
from django.utils import timezone


class City(models.Model):
    name = models.CharField('Shahar nomi', max_length=70, unique=True)
    slug = models.SlugField('Url')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Shahar'
        verbose_name_plural = 'Shaharlar'


class ProgrammingLanguage(models.Model):
    name = models.CharField('Dasturlash tili', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dasturlash tili'
        verbose_name_plural = 'Dasturlash tillari'


class Vacancy(models.Model):
    url = models.URLField(verbose_name='Ssilka', unique=True)
    title = models.CharField('Vakansiya sarlavhasi', max_length=250)
    company = models.CharField('Kompaniya', max_length=200)
    description = models.TextField('Opisaniya')
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name='Shahar', related_name='vacancies')
    programming_language = models.ForeignKey('ProgrammingLanguage', on_delete=models.CASCADE,
                                             verbose_name='Dasturlash tili', related_name='vacancies')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Vakansiya'
        verbose_name_plural = 'Vakansiyalar'