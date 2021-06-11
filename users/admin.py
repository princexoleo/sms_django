from django.contrib import admin
from .models import SubjectsModel, StudentsModel

# Register your models here.
@admin.register(SubjectsModel)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject_name', 'is_optional']
    list_filter = ['is_optional']
    search_fields = ['id', 'subject_name']


@admin.register(StudentsModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'student_roll', 'department_name',
                    'batch_session', 'created_user',
                    'subject_1', 'subject_2', 'subject_3', 'subject_4',
                    'subject_5', 'subject_6', 'subject_optional']
    list_filter = ['department_name', 'batch_session', 'created_user']
    search_fields = ['id', 'student_name', 'student_roll']

