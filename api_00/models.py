from django.db import models


# Create your models here.
# THE SAMPLE MODEL
class Records(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
