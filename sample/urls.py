from django.urls import path
from . import views

app_name='sample'
urlpatterns = [
    path('', views.sampleFromView, name="index")
]