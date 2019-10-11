from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=30)
    title_en=models.CharField(max_length=60)
    audience=models.IntegerField()
    open_date=models.DateTimeField(auto_now=True)
    genre=models.CharField(max_length=10)
    watch_grade=models.CharField(max_length=10)
    score=models.FloatField()
    poster_url=models.TextField()
    description=models.TextField()
  