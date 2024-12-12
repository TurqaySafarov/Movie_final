
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('',views.home,name='home'),
    path('logout/', views.logout, name='logout'),
    path('movie/<str:movie_link>/',views.moviepage,name='moviepage'),
    path('movie/<str:movie_link>/play',views.movieplayer,name='movieplayer'),
    path('series/<str:series_link>/',views.open_series,name='open_series'),
    path('series/<str:series_link>/<str:season_link>/<str:episode_link>/',views.play_series,name='play_series'),
    path('addWatchListFilm/<str:movie_link>/',views.addWatchListMovie,name='addwatchlistmovie'),
    path('form/',views.form,name='form'),
    path('addWatchListSeries/<str:series_link>/', views.addWatchListSeries, name='addwatchlistseries'),
    path('saveWatchTimeFilm/<str:movie_link>/<str:time>/',views.saveWatchTimeFilm,name='watchtimesavefilm'),
    path('saveWatchTimeSeries/<str:series_link>/<str:season_link>/<str:episode_link>/<str:time>/',views.saveWatchTimeSeries,name='watchtimesavefilm'),
    path('getEpisodes/<str:series_link>/<int:season_id>/',views.getEpisodes,name='GetEpisodes'),
    path('likeDiscussion/<int:discussion_id>/',views.likeDiscussion,name='discussionlike'),
    path('form/discussions/<str:discussion_film_link>/<str:discussion_header>/',views.discussion_page,name='dispage'),
    path('discussionCommentLike/<int:discussion_comment_id>',views.discussionCommentLike,name='discuscomlikelike'),
    path('form/discussions/<str:film_link>/',views.topicspage,name='topicpage')
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
