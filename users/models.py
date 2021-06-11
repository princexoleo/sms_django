from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.



class SubjectsModel(models.Model):
    """ There many subjects available in the college, and it varies accourding to departments"""
    id  = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    is_optional = models.BooleanField(default=False)
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.subject_name



# Students
class StudentsModel(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_roll = models.CharField(max_length=10)
    batch_session = models.CharField(max_length=20)
    department_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    created_user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject_1 = models.ForeignKey(SubjectsModel, on_delete=models.DO_NOTHING, related_name="sub_1")
    subject_2 = models.ForeignKey(SubjectsModel, on_delete=models.DO_NOTHING, related_name="sub_2")
    subject_3 = models.ForeignKey(SubjectsModel, on_delete=models.DO_NOTHING, related_name="sub_3")
    subject_4 = models.ForeignKey(SubjectsModel, on_delete=models.DO_NOTHING, related_name="sub_4")
    subject_5 = models.ForeignKey(SubjectsModel, on_delete=models.DO_NOTHING, related_name="sub_5")
    subject_6 = models.ForeignKey(SubjectsModel, on_delete=models.DO_NOTHING, related_name="sub_6")
    subject_optional = models.ForeignKey(SubjectsModel, on_delete=models.DO_NOTHING, related_name="sub_optional")
