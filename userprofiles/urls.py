from django.urls import path

from . import views

urlpatterns = [

    path('',views.userprofiles, name='userprofiles')
 

]