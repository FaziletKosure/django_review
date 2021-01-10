from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list),
    path('<int:pk>/', views.student_detail),
    path('home-api', views.home_api),
    path("list-api/", views.student_list_api),
    path("create-api/", views.student_create_api),
]
