from django.contrib import admin
from .models import games
# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display=('id','game_title','year','dowload_links')

admin.site.register(games,GameAdmin)
# admin.site.register(GameAdmin)
 