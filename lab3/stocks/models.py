from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название лекарства")
    disease = models.CharField(max_length=255, verbose_name="Назначение")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    prescript = models.BooleanField(verbose_name="Нужен рецепт?")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Когда последний раз обновлялась информация?")
# Create your models here.
