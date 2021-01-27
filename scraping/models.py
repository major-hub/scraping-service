from django.db import models


class City(models.Model):
    name = models.CharField('Shahar nomi', max_length=70)
    slug = models.SlugField('Url')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Shahar'
        verbose_name_plural = 'Shaharlar'
