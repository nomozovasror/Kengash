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
admin.site.register(VotingTimer)

# @admin.register(AllowedTeachers)
# class AllowedTeachersAdmin(admin.ModelAdmin):
#     raw_id_fields = ['teacher']  # Teacher maydoni uchun qidiruv oynasi
#     list_display = ['teacher', 'voter']

#
# @admin.register(Candidates)
# class CandidatesAdmin(admin.ModelAdmin):
#     raw_id_fields = ['teacher']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # Define search fields for autocomplete
    search_fields = ['full_name']
    # Optional: Display fields in the autocomplete dropdown
    list_display = ['full_name']

    def get_search_results(self, request, queryset, search_term):
        # Customize search for autocomplete
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if request.path == '/admin/autocomplete/':  # Ensure this applies to autocomplete
            queryset = queryset.filter(full_name__icontains=search_term)
        return queryset, use_distinct


@admin.register(SelectedEmployee)
class SelectedEmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee', 'type', 'status', 'voted', 'linked_employee']
    list_filter = ['status', 'voted']
    search_fields = ['employee__full_name']
    # Enable autocomplete for the employee field
    autocomplete_fields = ['employee', 'linked_employee']  # Include linked_employee if needed
    # Add custom action
    actions = ['reset_and_delete_votes']

    def reset_and_delete_votes(self, request, queryset):
        # Delete all related Vote objects
        Vote.objects.filter(employee__in=queryset).delete()
        # Reset status and voted to False
        queryset.update(status=False, voted=False)
        # Show success message
        self.message_user(request, "Selected employees' votes have been deleted and their status/voted fields reset to False.")

    reset_and_delete_votes.short_description = "Delete related votes and reset status/voted to False"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Optional: Limit the queryset for large datasets
        if db_field.name in ['employee', 'linked_employee']:
            kwargs['queryset'] = Employee.objects.all()  # Customize if needed
        return super().formfield_for_foreignkey(db_field, request, **kwargs)




