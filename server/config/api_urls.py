from django.urls import path, include

from apps.medical.routers import patient_router

urlpatterns = [
]

urlpatterns += patient_router.urls
