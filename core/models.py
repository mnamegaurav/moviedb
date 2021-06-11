from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    details = models.JSONField(verbose_name="Movie Details")
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('added_on', 'updated_on',)

    def __str__(self):
        return self.details.get('Title', 'N/A: Not Found')

    def save(self, *args, **kwargs):
        self.title = self.details.get('Title', '')
        return super().save(*args, **kwargs)


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('added_on', 'updated_on',)
