from rest_framework import serializers

from apps.medical.models import Patient


# Сериализатор для получение списка пациентов или одного пациента
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


# Сериализатор для создания и обновления пациента
class CreateUpdatePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'birthdate',
        ]

    # Определяем метод data как свойство,
    # чтобы после выполнение запроса получать данные в виде PatientSerializer
    @property
    def data(self):
        return PatientSerializer(
            instance=self.instance
        ).data
