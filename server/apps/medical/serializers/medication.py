from rest_framework import serializers

from apps.medical.models import Medication


# Сериализатор для получения списка медикаментов или одного медикамента
class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


# Сериализатор для создания и обновления медикамента
class CreateUpdateMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = [
            'name',
            'dosage',
            'price',
            'is_discounted',
        ]

    # Определяем метод data как свойство,
    # чтобы после выполнение запроса получать данные в виде MedicationSerializer
    @property
    def data(self):
        return MedicationSerializer(
            instance=self.instance
        ).data
