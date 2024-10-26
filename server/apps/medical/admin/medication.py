from django.contrib import admin

from ..models import Medication


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    pass
