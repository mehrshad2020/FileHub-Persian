from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('files/', views.FileListView.as_view(), name='file-list'),
    path('files/<int:pk>/', views.FileDetailView.as_view(), name='file-detail'),
    path('files/upload/', views.FileUploadView.as_view(), name='file-upload'),
    path('files/<int:pk>/delete/', views.FileDeleteView.as_view(), name='file-delete'),
] 