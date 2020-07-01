# models.py
from django.db import models

class Job(models.Model):
    """ Model for the job image and summary fields in Admin """
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        """ Provides a description of each job summary in Admin """
        return self.summary


