from typing import Type

from rest_framework import viewsets, serializers

from apps.medical.models import Prescription
from apps.medical.serializers import PrescriptionSerializer, CreateUpdatePrescriptionSerializer


# Класс PrescriptionViewSet  наследуется от класса ModelViewSet
# Включает в себе базовую логику CRUD при обращении к API запросами GET, POST, PUT, PATCH и DELETE
class PrescriptionViewSet(viewsets.ModelViewSet):

    # Словарь SERIALIZER_CLASS_MAP для хранения классов сериализаторов относительно метода
    SERIALIZER_CLASS_MAP = {
        'list': PrescriptionSerializer,
        'retrieve': PrescriptionSerializer,
        'create': CreateUpdatePrescriptionSerializer,
        'update': CreateUpdatePrescriptionSerializer,
    }

    def get_serializer_class(self) -> Type[serializers.ModelSerializer]:
        return self.SERIALIZER_CLASS_MAP.get(self.action, PrescriptionSerializer)

    def get_queryset(self):
        queryset = Prescription.objects.all()  # Получаем все объекты модели Prescription
        return queryset
