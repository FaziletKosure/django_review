from django.urls import path
from . import views

app_name = 'fscohort'

urlpatterns = [
    path('', views.index, name='index'),
    path('num/', views.student_num, name='student_num'),
    path('add/', views.student_add, name='student_add'),
    path('<int:id>', views.student_detail, name='student_detail'),
]
