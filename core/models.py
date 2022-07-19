from django.db import models

class ITA_Words(models.Model):
    ita = models.CharField(max_length=100)
    eng = models.CharField(max_length=100)