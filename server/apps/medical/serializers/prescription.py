from rest_framework import serializers

from apps.medical.models import Prescription

from .patient import PatientSerializer
from .medication import MedicationSerializer


# Сериализатор для получения списка рецептов или одного рецепта
class PrescriptionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    medication = MedicationSerializer()

    class Meta:
        model = Prescription
        fields = [
            'id',
            'dosage',
            'patient',
            'medication',
        ]


# Сериализатор для создания и обновления пациента
class CreateUpdatePrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = [
            'dosage',
            'patient',
            'medication',
        ]

    # Определяем метод data как свойство,
    # чтобы после выполнение запроса получать данные в виде PrescriptionSerializer
    @property
    def data(self):
        return PrescriptionSerializer(
            instance=self.instance
        ).data
