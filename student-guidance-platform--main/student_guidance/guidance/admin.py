
from django.contrib import admin
from .models import Student, CareerProgress


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_number', 'branch', 'year', 'created_at')
    search_fields = ('user__username', 'roll_number', 'branch')
    list_filter = ('branch', 'year', 'created_at')


@admin.register(CareerProgress)
class CareerProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'selected_career_goal', 'completed_projects', 'certifications')
    search_fields = ('student__user__username',)
