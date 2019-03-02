from django.urls import path
from . import  views

urlpatterns = [
    path('',views.upload1)
    #,path('',views.show_files)
]