from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Gender)
admin.site.register(AcademicDegree)
admin.site.register(AcademicRank)
admin.site.register(StructureType)
admin.site.register(LocalityType)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(EmploymentForm)
admin.site.register(EmploymentStaff)
admin.site.register(StaffPosition)
admin.site.register(EmployeeStatus)
admin.site.register(EmployeeType)
admin.site.register(Vote)

# @admin.register(AllowedTeachers)
# class AllowedTeachersAdmin(admin.ModelAdmin):
#     raw_id_fields = ['teacher']  # Teacher maydoni uchun qidiruv oynasi
#     list_display = ['teacher', 'voter']

#
# @admin.register(Candidates)
# class CandidatesAdmin(admin.ModelAdmin):
#     raw_id_fields = ['teacher']

@admin.register(SelectedEmployee)
class SelectedEmployeeAdmin(admin.ModelAdmin):
    raw_id_fields = ['employee']
    list_display = ['employee']



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['full_name']


