from django.urls import path
from .views import *

app_name = 'teachers'
urlpatterns = [
    path("update-employee/", update_and_save_employee, name='update_employee'),
    path('', home, name='home'),
    path('finish/', finish_vote, name='finish_vote'),
    path('start-vote/', start_vote, name='start_vote'),
    path('vote/', VoteView.as_view(), name='vote'),

    path('start/', start, name='start'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/dashboard-data/', get_dashboard_data, name='get_dashboard_data'),
    path('dashboard/result', get_result, name='get_result'),
    path('api/result-data/', get_result_data, name='get_result_data'),

    path('download-results/', generate_vote_results_docx, name='download_results'),

    path('save_timer/', save_timer, name='save_timer'),
    path('get_timer/', get_timer, name='get_timer'),




    path('update_employee_status/', UpdateEmployeeStatusView.as_view(), name='update_employee_status'),
    path('start_vote/', start_vote, name='start_vote'),

    path('get_vote_data/', get_vote_data, name='get_vote_data'),

    path('reset_all_status/', reset_all_status, name='reset_all_status'),
]
