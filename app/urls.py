from app.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('aku/',aku,name='aku'),
]