from django.contrib import admin
from .models import *
# Register your models here.


# Correct registration of UsersApp with UsersAppAdmin
class UsersAppAdmin(admin.ModelAdmin):
    list_filter = ['email']
    search_fields = ['email','username','password']
    list_display = ['email','username','password']

# Register UsersApp with the custom UsersAppAdmin class
admin.site.register(UsersApp, UsersAppAdmin)


# Correct registration of UsersApp with UsersAppAdmin
class FilmAdmin(admin.ModelAdmin):
    search_fields = ['film_name','film_director','film_genre','film_category',]
    list_display = ['film_name','film_director','film_genre','film_category',]
 
# Register UsersApp with the custom UsersAppAdmin class
admin.site.register(Film, FilmAdmin)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['series_name','series_director','series_genre','series_category','series_episode_count']
    search_fields = ['series_name','series_director','series_genre','series_category','series_episode_count']

    
# Register UsersApp with the custom UsersAppAdmin class
admin.site.register(Series, SeriesAdmin)

class SeriesSeasonsAdmin(admin.ModelAdmin):
    list_display = ['series__series_name','series_seasons_name','series_seasons_number','series_seasons_poster','series_seasons_trailer']
    search_fields  = ['series__series_name','series_seasons_name','series_seasons_number','series_seasons_poster','series_seasons_trailer']


admin.site.register(SeriesSeasons, SeriesSeasonsAdmin)

class SeriesEpisodesAdmin(admin.ModelAdmin):
    list_display = ['series_seasons', 'series_episodes_name','series_episodes_number' ]
    search_fields = ['series_episodes_name','series_episodes_number']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            # Access the `series` field value from the existing sss
            series = obj.series
            # Perform any additional logic with `series`
        return form
    

class DiscussionsAdmin(admin.ModelAdmin):
    list_display = ['user__username' , 'discussion_film','discussion_likes','discussion_replies']
    search_fields = ['user__username' , 'user__email' , 'discussion_film__film_name','discussion_likes','discussion_replies']
admin.site.register(SeriesEpisodes, SeriesEpisodesAdmin)
admin.site.register(WatchList)
admin.site.register(UserLikeList)
admin.site.register(Discussion,DiscussionsAdmin)
admin.site.register(DiscussionComments)