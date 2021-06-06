from django import forms 
from django.forms import Form
from student_management_app.models import DepartmentModel, SubjectsModel, SessionYearModel


class DateInput(forms.DateInput):
    input_type = "date"



# Add Students Forms
class AddStudentForm(forms.Form):
    student_name = forms.CharField(label="Student Name", max_length=255, widget=forms.TextInput(attrs={"class":"form-control"}))
    student_roll = forms.CharField(label="Student Roll", max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
    
    
    # Displaying Departments
    try:
        department_list = []
        departments = DepartmentModel.objects.all()
        for dept in departments:
            single_dept = (dept.id, dept.department_name)
            department_list.append(single_dept)
    except :
        department_list = []
    

    # Displaying the sessopm
    try:
        session_list = []
        sessions_year = SessionYearModel.objects.all() 
        for session_year in sessions_year:
            single_session = (session_year.id, str(session_year.session_start_year)+"to"+str(session_year.session_end_year))
            session_list.append(single_session)

    except:
        session_list = []
    
    #
    department_id = forms.ChoiceField(label="Department", choices=department_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year",hoices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))



# Eiditing the students information
class EditStudentForm(forms.Form):
    student_name = forms.CharField(label="Student Name", max_length=255, widget=forms.TextInput(attrs={"class":"form-control"}))
    student_roll = forms.CharField(label="Student Roll", max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
    
    
    # Displaying Departments
    try:
        department_list = []
        departments = DepartmentModel.objects.all()
        for dept in departments:
            single_dept = (dept.id, dept.department_name)
            department_list.append(single_dept)
    except :
        department_list = []
    

    # Displaying the sessopm
    try:
        session_list = []
        sessions_year = SessionYearModel.objects.all() 
        for session_year in sessions_year:
            single_session = (session_year.id, str(session_year.session_start_year)+"to"+str(session_year.session_end_year))
            session_list.append(single_session)

    except:
        session_list = []
    
    #
    department_id = forms.ChoiceField(label="Department", choices=department_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year",hoices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
