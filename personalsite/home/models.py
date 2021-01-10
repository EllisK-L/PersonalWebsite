from django.db import models

class Experience(models.Model):
    heading = models.CharField(max_length=30)
    content = models.CharField(max_length=30000)
    typeof = models.CharField(max_length=15)