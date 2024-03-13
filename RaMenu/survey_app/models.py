from django.db import models
from django.contrib.auth.models import User
from desire_app.models import Desire

# Create your models here.

class Preference(models.Model):
    user = models.ForeignKey(User, related_name='preferences',on_delete=models.CASCADE)
    code = models.CharField(max_length=256)
    desire = models.ForeignKey(Desire, related_name='preferences', on_delete=models.CASCADE)
    answer = models.CharField(max_length=128) #yes, maybe, no

