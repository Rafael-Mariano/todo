from django.db import models

# Create your models here.
class Things(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    data = models.DateField()

    def __str__(self):
        return self.title