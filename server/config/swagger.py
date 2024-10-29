from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

api_info = openapi.Info(
    title="Учет льготных лекарств",
    default_version='v1',
    description="API информационной системы районной поликлиники. Учет льготных лекарств.",
    license=openapi.License(name="BSD License"),
)
schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=[permissions.AllowAny],
)
