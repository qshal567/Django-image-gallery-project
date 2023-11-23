# image_gallery_app/models.py
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title
