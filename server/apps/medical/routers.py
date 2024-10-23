from rest_framework.routers import DefaultRouter

from .viewsets import PatientViewSet, MedicationViewSet


patient_router = DefaultRouter()
medications_router = DefaultRouter()

patient_router.register(
    r'patients',
    PatientViewSet,
    basename='patient'
)
medications_router.register(
    r'medications',
    MedicationViewSet,
    basename='medication',
)

