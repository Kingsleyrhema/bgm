from django.urls import path
from . views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('about',about, name='about'),
    path('contact',contact, name='contact'),
    path('contact',signup, name='signup'),
    path('activities',activity, name='activities')
]