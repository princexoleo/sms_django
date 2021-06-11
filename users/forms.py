from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import SubjectsModel, StudentsModel
from django.forms.widgets import Select
 
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']



class SubjectForm(forms.ModelForm):
    subject_name = forms.CharField(
        label='',
        max_length=30,
        min_length=2,
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
def get_available_optional_subject():
    avialable_optional = SubjectsModel.objects.all().filter(is_optional=True)
    choices = ()
    for i,sub in enumerate(avialable_optional):
        choices = choices + ((int(sub.id), sub.subject_name),)
    return choices

class StudentForm(forms.ModelForm):
    dept_choices = ( 
        ('science', 'Science'),
        ('huminities', 'Humanities'),
        ('business studies', 'Business Studies'),
    )
    batch_choice = (
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
    )

    #subject_optional = forms.ChoiceField(choices=get_available_optional_subject())
    department_name = forms.ChoiceField(choices=dept_choices)
    batch_session = forms.ChoiceField(choices=batch_choice)
    class Meta:
        model = StudentsModel
        fields = ['student_name', 'student_roll','batch_session','department_name',
                  'subject_1', 'subject_2', 'subject_3', 'subject_4', 'subject_5',
                  'subject_6', 'subject_optional']

