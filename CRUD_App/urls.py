from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("register/", views.register_user, name='register_user'),
    path("records/<int:pk>", views.customer_record, name='record'),
    path("delete_records/<int:pk>", views.delete_record, name='delete_record'),
    path("add_records/", views.add_records, name='add_records'),
]