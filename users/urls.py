from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='users/home.html'), name ='logout'),
    path('register/', views.register, name ='register'),
]