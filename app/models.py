from django.db import models
import datetime
# Create your models here.


class UsersApp(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.email


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    film_link = models.CharField(max_length=100,default='')
    film_name = models.CharField(max_length=100)
    film_director = models.CharField(max_length=100)
    film_category = models.CharField(max_length=100)
    film_genre = models.CharField(max_length=100)
    release_date = models.DateField()
    film_duration = models.DurationField()
    film_description = models.TextField()
    film_poster = models.ImageField(upload_to='film_posters/',default='')
    film_trailer = models.URLField(default='')
    film_video = models.FileField(upload_to='film_videos/', default='')
    film_cast = models.JSONField()
    movie_open_image = models.ImageField(upload_to='film_open_images/', default='')
    film_imdb_rating = models.FloatField(default=0.0)
    watch_count = models.IntegerField(default=0)
    discussion_count = models.IntegerField(default=0)
    review_count = models.IntegerField(default=0)
    def __str__(self):
        return self.film_name

class Series(models.Model):
    series_id = models.AutoField(primary_key=True)
    series_name = models.CharField(max_length=100)
    series_director = models.CharField(max_length=100)
    series_category = models.CharField(max_length=100)
    series_genre = models.CharField(max_length=100)
    release_date = models.DateField()
    series_link = models.CharField(max_length=100, default='')
    series_description = models.TextField()
    series_episode_count = models.IntegerField(default=0)
    series_open_poster = models.ImageField(upload_to='series_open_posters/', default='')
    series_poster = models.ImageField(upload_to='series_posters/', default='')
    series_trailer = models.URLField(default='')
    series_cast = models.JSONField()
    series_season_id = models.IntegerField(default=0)
    series_imdb_rating = models.FloatField(default=0.0)
    watch_count = models.IntegerField(default=0)
    def __str__(self):
        return self.series_name

class SeriesSeasons(models.Model):
    series_seasons_id = models.AutoField(primary_key=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE,default=0)  
    series_seasons_name = models.CharField(max_length=100)
    series_seasons_number = models.IntegerField()
    series_seasons_description = models.TextField()
    series_seasons_poster = models.ImageField(upload_to='series_seasons_posters/', default='')
    series_seasons_trailer = models.URLField(default='')
    series_season_episode_count = models.IntegerField(default=0)
    series_seasons_link = models.CharField(max_length=100, default='')
    def __str__(self):
        return  self.series.series_name + '-' +self.series_seasons_name 

class SeriesEpisodes(models.Model):
    series_episodes_id = models.AutoField(primary_key=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, default=0)
    series_episode_link = models.CharField(max_length=100, default='')
    series_seasons = models.ForeignKey(SeriesSeasons, on_delete=models.CASCADE, default=0)  
    series_episodes_name = models.CharField(max_length=100)
    series_episodes_number = models.IntegerField()
    series_episodes_description = models.TextField()
    series_episodes_poster = models.ImageField(upload_to='series_episodes_posters/', default='')
    series_episode_video = models.FileField(upload_to='series_episode_videos/', default='')
    episode_duration = models.DurationField(default=datetime.timedelta(minutes=0))
    series_episodes_trailer = models.URLField(default='')
    def __str__(self):
        return self.series_episodes_name
    
    
    
class ContinueWatchingFilm(models.Model):
    continue_watching_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UsersApp, on_delete=models.CASCADE, default=0)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=0)
    continue_watching_time = models.DurationField(default=datetime.timedelta(minutes=0))
    def __str__(self):
        return self.user.username + '-' + self.film.film_name 
    

class ContinueWatchingSeries(models.Model):
    continue_watching_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UsersApp, on_delete=models.CASCADE, default=0)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, default=0)
    serie_season = models.ForeignKey(SeriesSeasons, on_delete=models.CASCADE, default=0)
    serie_episode = models.ForeignKey(SeriesEpisodes, on_delete=models.CASCADE, default=0)
    continue_watching_time = models.DurationField(default=datetime.timedelta(minutes=0))
    def __str__(self):
        return self.user.username + '-' + self.series.series_name
    
    
class UserLikeList(models.Model):
    like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UsersApp, on_delete=models.CASCADE, default=0)
    likelist = models.JSONField(default={"films": [], "series": []})
    def __str__(self):
        return self.user.username 
    
    
class WatchList(models.Model):
    watchlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UsersApp, on_delete=models.CASCADE, default=0)
    watchlist = models.JSONField(default={"films": [], "series": []})
    def __str__(self):
        return self.user.username
    
    
    
class Discussion(models.Model):
    discussion_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UsersApp, on_delete=models.CASCADE, default=0)
    discussion_film = models.ForeignKey(Film, on_delete=models.CASCADE, default=0)
    discussion_header = models.CharField(max_length=1000)
    discussion_content = models.TextField()
    discussion_date = models.DateTimeField(auto_now_add=True)
    discussion_likes = models.IntegerField(default=0)
    discussion_replies = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username + '-' + self.discussion_film.film_name
    
    
class DiscussionLikes(models.Model):
    discussion_like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UsersApp, on_delete=models.CASCADE, default=0)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.user.username + '-' + self.discussion.discussion_content

class DiscussionComments(models.Model):
    discussion_comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UsersApp, on_delete=models.CASCADE, default=0)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, default=0)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    discussion_comment_content = models.TextField()
    discussion_comment_date = models.DateTimeField(auto_now_add=True)
    discussion_comment_likes = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username + '-' + self.discussion_comment_content

class DiscussionCommentLikes(models.Model):
    discussion_comment_like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UsersApp, on_delete=models.CASCADE, default=0)
    discussion_comment = models.ForeignKey(DiscussionComments, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.user.username + '-' + self.discussion_comment.discussion_comment_content