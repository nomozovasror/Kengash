from django.urls import path
from .views import *

app_name = 'teachers'
urlpatterns = [
    path("update-employee/", update_and_save_employee, name='update_employee'),
    path('', home, name='home'),
    path('finish/', finish_vote, name='finish_vote'),
    path('start-vote/', start_vote, name='start_vote'),
    path('vote/', VoteView.as_view(), name='vote'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/dashboard-data/', get_dashboard_data, name='get_dashboard_data'),
    path('download-results/', generate_vote_results_docx, name='download_results'),
]
