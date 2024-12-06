from django.urls import path
from . import views

app_name = 'teachers'
urlpatterns = [
    path("update-employee/", views.update_and_save_employee, name='update_employee'),
    path('', views.webapp_view, name='webapp'),
    path('quiz/', views.StartQuiz.as_view(), name='start_quiz'),
    path('result/', views.result, name='result'),
    path('table-result/', views.TableResult.as_view(), name='table_result')
]
