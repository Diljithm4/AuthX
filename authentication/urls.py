from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('timer/', views.timer_page, name='timer_page'),
    path('auth/login/', views.login, name='login'),
]