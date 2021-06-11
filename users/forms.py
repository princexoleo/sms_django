from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import SubjectsModel, StudentsModel
 
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']



class SubjectsForm(forms.Form):
    ubject_name = forms.CharField(
        label='',
        max_length=30,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Subject Name",
                "class": "form-control"
            }
        )
    )
    is_optional = forms.BooleanField(
        required=False,
        label="Check the box if it is optional subjects",
        widget= forms.CheckboxInput(
            attrs={
                "class": "form-control"
            })
    )

    class Meta:
        model = SubjectsModel
        fields = ['subject_name','is_optional']


## StudentModels forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentsModel
        fields = ['student_name', 'student_roll','batch_session','department_name',
                  'subject_1', 'subject_2', 'subject_3', 'subject_4', 'subject_5',
                  'subject_6', 'subject_optional', 'created_user']