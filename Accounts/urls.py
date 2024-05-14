from django.urls import path
from .views import *
urlpatterns = [
    path('Login/', login_user,name= 'login'),
    path('Logout/', logout_user,name= 'logout'),
    path('Register/', register_user,name='register'),
]