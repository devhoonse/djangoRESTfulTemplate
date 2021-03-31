from django.db import models


# Create your models here.
# THE SAMPLE MODEL
class Record(models.Model):
    rid = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
