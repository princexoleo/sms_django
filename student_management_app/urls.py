from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login_page, name='login'),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('logout', views.logout_user, name='logout'),
]