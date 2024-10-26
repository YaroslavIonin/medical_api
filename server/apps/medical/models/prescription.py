from django.db import models

from .patient import Patient

from .medication import Medication


class Prescription(models.Model):
    """Модель рецепта"""
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name='Пациент',
    )
    medication = models.ForeignKey(
        Medication,
        on_delete=models.CASCADE,
        verbose_name='Медикамент',
    )
    dosage = models.CharField(
        max_length=50,
        verbose_name='Дозировка',
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.patient} {self.medication} {self.dosage}'
