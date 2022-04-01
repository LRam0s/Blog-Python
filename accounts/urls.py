from django.urls import path
from .views import inicio,mi_login, signup, editar
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('',inicio, name='inicio'),
    path('login/', mi_login, name='login'),
    path('signup/', signup, name = 'signup'),
    path('logout/', LogoutView.as_view(template_name= 'accounts/logout.html'), name = 'logout'),
    path('edit/', editar , name='edit'),
    
]