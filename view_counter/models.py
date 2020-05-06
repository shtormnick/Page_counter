from django.db import models

# Create your models here.

class Page(models.Model):
    title_name = models.CharField(max_length=100, unique=False)
    description = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return self.title_name

    