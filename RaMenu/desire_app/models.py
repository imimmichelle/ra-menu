from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=1024)

    def __str__(self):
        return self.category_name

class Desire(models.Model):
    desire_name = models.CharField(max_length=1024)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.desire_name