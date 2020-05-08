from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=100, unique=False)
    description = models.CharField(max_length=264, unique=False)

    def __str__(self):
        page = '{0.title} {0.description}'
        return page.format(self)

class Counter(models.Model):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return 'counter for ' + self.page.title