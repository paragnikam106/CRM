from django.urls import path
from .import views
urlpatterns = [
    path('',views.main,name='main'),
     path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('tracking',views.tracking,name='tracking'),
    path('addrecord',views.add,name='addrecord'),
    path('updaterecord/<int:pk>',views.updaterecord,name='updaterecord'),
    path('deleterecord/<int:pk>',views.delete,name='deleterecord'),
   
]