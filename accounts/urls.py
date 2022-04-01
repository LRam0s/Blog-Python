from django.urls import path
from .views import inicio,mi_login, signup



urlpatterns = [
    path('',inicio, name='inicio'),
    path('login/', mi_login, name='login'),
    path('signup/', signup, name = 'signup')
    
]