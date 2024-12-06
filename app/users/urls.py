from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path("login/", LoginView.as_view(), name="login_page"),
    path('hemis-teacher/', hemis_login_teacher, name="hemis_login_teacher"),
    path('auth/', auth, name='auth'),
    path('logout/', logout, name='logout'),
]