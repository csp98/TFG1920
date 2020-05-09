from django.urls import path

from . import views

urlpatterns = [
    path('assign/', views.assign, name='assign'),
    path('unassign/', views.unassign, name='unassign'),
    path('view/', views.view, name='view'),
]