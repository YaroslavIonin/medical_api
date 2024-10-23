from typing import Type

from rest_framework import viewsets, serializers

from apps.medical.models import Patient
from apps.medical.serializers import PatientSerializer, CreateUpdatePatientSerializer


# Класс PatientViewSet  наследуется от класса ModelViewSet
# Включает в себе базовую логику CRUD при обращении к API запросами GET, POST, PUT, PATCH и DELETE
class PatientViewSet(viewsets.ModelViewSet):

    # Словарь SERIALIZER_CLASS_MAP для хранения классов сериализаторов относительно метода
    SERIALIZER_CLASS_MAP = {
        'list': PatientSerializer,
        'retrieve': PatientSerializer,
        'create': CreateUpdatePatientSerializer,
        'update': CreateUpdatePatientSerializer,
    }

    def get_serializer_class(self) -> Type[serializers.ModelSerializer]:
        return self.SERIALIZER_CLASS_MAP.get(self.action, PatientSerializer)

    def get_queryset(self):
        queryset = Patient.objects.all()  # Получаем все объекты модели Patient
        return queryset
