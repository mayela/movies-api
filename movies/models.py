from django.db import models


class Artist(models.Model):
    first_name = models.CharField('First name', max_length=80)
    last_name = models.CharField('Last name', max_length=150)


class Movie(models.Model):
    title = models.CharField('Title', max_length=150)
    synopsis = models.TextField('Synopsis')
    year = models.PositiveSmallIntegerField('Year')
    artists = models.ManyToManyField(
        Artist,
        related_name='movies',
        blank=True,
        null=True
    )
