from typing import Type

from rest_framework import viewsets, serializers

from apps.medical.models import Medication
from apps.medical.serializers import MedicationSerializer, CreateUpdateMedicationSerializer


# Класс MedicationViewSet  наследуется от класса ModelViewSet
# Включает в себе базовую логику CRUD при обращении к API запросами GET, POST, PUT, PATCH и DELETE
class MedicationViewSet(viewsets.ModelViewSet):

    # Словарь SERIALIZER_CLASS_MAP для хранения классов сериализаторов относительно метода
    SERIALIZER_CLASS_MAP = {
        'list': MedicationSerializer,
        'retrieve': MedicationSerializer,
        'create': CreateUpdateMedicationSerializer,
        'update': CreateUpdateMedicationSerializer,
    }

    def get_serializer_class(self) -> Type[serializers.ModelSerializer]:
        return self.SERIALIZER_CLASS_MAP.get(self.action, MedicationSerializer)

    def get_queryset(self):
        queryset = Medication.objects.all()  # Получаем все объекты модели Patient
        return queryset
