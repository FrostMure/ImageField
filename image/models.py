from django.db import models

# Create your models here.

class imagen(models.Model):
    image = models.ImageField(blank=True, upload_to="test/", null=True)
    name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"imagen: {self.category}"