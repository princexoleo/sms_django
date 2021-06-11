from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


from datetime import datetime
from .models import SubjectsModel, StudentsModel
from .forms import SubjectForm, StudentForm
# Create your views here.#################### index#######################################


def home(request):
    return render(request, 'users/home.html', {'title':'index'})
  
########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('users/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title':'reqister here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form, 'title':'log in'})



def dashboard(request):
    subjects_list = SubjectsModel.objects.all()
    subjects = {
        "subjects": subjects_list,
    }
    return render(request, 'users/dashboard.html', subjects) 


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            #print(form)
            # form.create_subject = request.user.id
            form.created_at = datetime.now()
            
            #print("Selected opt: ",form.cleaned_data['subject_optional'])
            #opt_subject = SubjectsModel.objects.get(id=form.cleaned_data['subject_optional'].id)
            #print("OptionalSubjects id: is = ", opt_subject)
            #form.subject_optional = opt_subject
            form.created_user = request.user.id
            form.save()
            messages.success(request, "Student Added successfully")
            return redirect('dashboard')
        else:
            messages.error(request, 'Correct the errors below')
    else:
        form = StudentForm()
    return render(request, "users/add_student.html", {'form': form})

def add_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            #print(form)
            # form.create_subject = request.user.id
            form.created_at = datetime.now()
            form.save()
            messages.success(request, "Subject Added successfully")
            return redirect('dashboard')
        else:
            messages.error(request, 'Correct the errors below')
    else:
        form = SubjectForm()
    return render(request, "users/add_subject.html", {'form': form})