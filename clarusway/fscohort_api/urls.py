from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list),
    path('<int:pk>/', views.student_detail),
]
