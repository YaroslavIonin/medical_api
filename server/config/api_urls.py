from django.urls import path, include

from apps.medical.routers import patient_router, medications_router, prescriptions_router

urlpatterns = [
]

urlpatterns += patient_router.urls
urlpatterns += medications_router.urls
urlpatterns += prescriptions_router.urls
