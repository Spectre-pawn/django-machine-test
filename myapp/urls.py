from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name="index" ),
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('clients/<int:pk>/update/', views.client_update, name='client_update'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('clients/<int:pk>/projects/create/', views.project_create, name='project_create'),
    path('projects/', views.project_list, name='project_list'),
]
