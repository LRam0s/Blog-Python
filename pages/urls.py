from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.PagesList.as_view(), name='list_pages'),
    path('crear/', views.CreatePages.as_view(), name = 'create_pages'),
    path('<int:pk>/', views.DetailPages.as_view(), name = 'detail_pages'),
    path('<int:pk>/editar/', views.EditPages.as_view(), name = 'edit_pages'),
    path('<int:pk>/borrar/', views.DeletePages.as_view(), name= 'delete_pages'),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)