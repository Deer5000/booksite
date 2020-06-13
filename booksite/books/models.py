from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    num_pages = models.IntegerField()
    date_published = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

