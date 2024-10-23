from rest_framework.routers import DefaultRouter

from .viewsets import PatientViewSet


patient_router = DefaultRouter()

patient_router.register(
    r'patients',
    PatientViewSet,
    basename='patient'
)

