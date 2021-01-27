from django.contrib import admin

from scraping.models import City, ProgrammingLanguage, Vacancy


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'city', 'programming_language')
    list_display_links = ('title', )
    search_fields = ('title', 'company', 'city', 'programming_language')
    list_filter = ('city', 'programming_language')
