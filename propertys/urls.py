from django.urls import path
from . import views


urlpatterns = [
    path('', views.PropertyListView.as_view(), name='property_list'),
    path('<int:pk>/', views.PropertyDetailView.as_view(), name='property_detail'),
    path('<int:pk>/update/', views.PropertyUpdateView.as_view(), name='property_update'),
    path('<int:pk>/delete/', views.PropertyDeleteView.as_view(), name='property_delete'),
    path('create/', views.PropertyCreateView.as_view(), name='property_create')
]
