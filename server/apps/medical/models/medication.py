from django.db import models


# Модель медикамента
class Medication(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название лекарства',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
    )
    is_discounted = models.BooleanField(
        default=False,
        verbose_name='Льготное лекарство',
    )

    class Meta:
        verbose_name = 'Медикамент'
        verbose_name_plural = 'Медикаменты'
        ordering = ['name']

    def __str__(self):
        return self.name
