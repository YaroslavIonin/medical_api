from django.urls import path, include

from apps.medical.routers import patient_router, medications_router

urlpatterns = [
]

urlpatterns += patient_router.urls
urlpatterns += medications_router.urls
