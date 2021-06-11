from django.db import models

# Create your models here.


class Movie(models.Model):
    details = models.JSONField(verbose_name="Movie Details")
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['added_on', 'updated_on']

    def __str__(self):
        return self.details.get('Title', 'N/A: Not Found')


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['added_on', 'updated_on']
