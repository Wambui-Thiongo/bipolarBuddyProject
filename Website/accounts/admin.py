from django.contrib import admin
from .models import CustomUser, Patient, Doctor, PatientKin

class PatientKinInline(admin.TabularInline):
    model=PatientKin
    extra=0

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display=['email','first_name','last_name','age','is_active','is_staff']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    inlines=[PatientKinInline]
    list_display=['user','doctor']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=['user','specialization']

@admin.register(PatientKin)
class PatientKinAdmin(admin.ModelAdmin):
    list_display=['user', 'patient', 'relation']