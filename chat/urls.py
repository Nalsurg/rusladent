from django.urls import path 
from . import views 

urlpatterns = [
    # path('', views.lobby)
    path('getEvents', views.getEvents, name='getEvents'),
    path('', views.EventFormView.as_view(), name='form_view'),
]