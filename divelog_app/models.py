from django.db import models

class Dive(models.Model):
    dive_title = models.CharField('dive title', max_length=200)
    dive_date = models.DateTimeField('date of dive')
