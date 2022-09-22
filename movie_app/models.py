from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
       return self.name


class Movie(models.Model):
    movie = models.ForeignKey(
        to=Director,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='review'
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    duration = models.CharField(max_length=10)
    director = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Review(models.Model):
    review = models.ForeignKey(
        to=Movie,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='review'
    )

    text = models.TextField(blank=True,null=True)
    movie = models.CharField(max_length=100)
    def __str__(self):
       return self.text