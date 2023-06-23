from django.urls import path
from employes import views


urlpatterns = [
    path('', views.EmployesView.as_view(), name='employes'),
    path('<int:pk>/', views.EmployesDetailView.as_view(), name='employes-detail'),
]