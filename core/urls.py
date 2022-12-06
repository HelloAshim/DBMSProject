from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('school/', views.school_list, name='school_list'),
    path('create-school/', views.create_school, name='create_school'),
   

]