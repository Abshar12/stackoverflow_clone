from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question