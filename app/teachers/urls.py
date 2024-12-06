from django.urls import path
from . import views

app_name = 'teachers'
urlpatterns = [
    path("update-employee/", views.update_and_save_employee, name='update_employee'),
    path('', views.webapp_view, name='webapp'),
]
