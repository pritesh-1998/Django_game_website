from django.contrib import admin
from .models import Genre,Movie
# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
admin.site.register(Genre,GenreAdmin)
class MovieAdmin(admin.ModelAdmin):
    list_display=('id', 'title','release','number_in_stock','daily_rate')
admin.site.register(Movie,MovieAdmin)


