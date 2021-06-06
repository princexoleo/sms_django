from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


# Admin Model
class AdminModelHOD(models.Model):
    """ Head of Department can be an admin """
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


# Stuff who can edit/update/ the students information according to subjects
class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


# Session Year model
class SessionYearModel(models.Model):
    """ In every college a session start from a date and end to a date. """
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateTimeField()
    session_end_year = models.DateTimeField() 
    objects = models.Manager()



# Department model

class DepartmentModel(models.Model):
    """ Every college has a department. i.e. Science, Humanities, Business Studies"""
    id = models.AutoField(primary_key=True) 
    department_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    


# Course/Subjects model
class SubjectsModel(models.Model):
    """ There many subjects available in the college, and it varies accourding to departments"""
    id  = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    department_id = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, default=1)
    is_optional = models.BooleanField(default=False)
    staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()




# Section model not need to apply now


# Students Model
class StudentModel(models.Model):
    """ Currently we collect the basic student information """
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=255)
    student_roll = models.CharField(max_length=20)
    department_id = models.ForeignKey(DepartmentModel, on_delete=models.DO_NOTHING, default=1)
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()




# Students Result Models

class StudentResult(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(SubjectsModel, on_delete=models.CASCADE)
    subject_exam_marks = models.FloatField(default=0)
    subject_assignment_marks = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



# Students Result Models


# Creating Django Signal
# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminModelHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 3:
            StudentModel.objects.create(admin=instance, department_id=DepartmentModel.objects.get(id=1), session_year_id=SessionYearModel.objects.get(id=1), address="", profile_pic="", gender="")
    


#
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminmodelhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.studentmodel.save()
