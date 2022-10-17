from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Sneakers(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sneakers'