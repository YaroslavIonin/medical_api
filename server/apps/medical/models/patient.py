from django.db import models


# Модель пациента
class Patient(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя пациента',
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия пациента',
    )
    birthdate = models.DateField(
        verbose_name='Дата рождения пациента',
    )

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
