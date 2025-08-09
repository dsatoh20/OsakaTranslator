from django.urls import path
from . import views

urlpatterns = [
    path('v1/translate/', views.index, name='callback'),
]
