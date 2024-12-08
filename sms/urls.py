from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_sms_view, name='send_sms'),
]
