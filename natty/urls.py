from django.urls import path
from . import views

urlpatterns = [  # Corrected variable name to 'urlpatterns'
    path('', views.index, name='index'),  # No spaces after '' in the path
]
