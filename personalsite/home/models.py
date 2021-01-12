from django.db import models

class Experience(models.Model):
    heading = models.CharField(max_length=125)
    subHeading = models.CharField(max_length=125, blank=True, null=True)
    content = models.TextField()
    typeof = models.CharField(max_length=15)
    photo = models.ImageField(upload_to="home", blank=True, null=True)