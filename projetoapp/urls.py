from django.urls import path
from projetoapp import views
urlpatterns=[
   path('', views.home, name='')
]