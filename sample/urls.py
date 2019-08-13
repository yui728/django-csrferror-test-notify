from django.urls import path
from . import views

app_name='sample'
urlpatterns = [
    path('', views.SampleFormView, name="sample_form")
]