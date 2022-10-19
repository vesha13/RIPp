from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Medicines(models.Model):
    name = models.CharField(max_length=30)
    disease = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'medicines'


class Clients(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'clients'

class Charts(models.Model):
    order_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'chart'

