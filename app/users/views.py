import os

from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from authlib.integrations.django_client import OAuth
import requests
from django.urls import reverse
from django.views import View

from users.models import CustomUser

from teachers.models import AllowedTeachers

oauth = OAuth()

oauth.register(
    name='teacher',
    client_id=os.environ.get('OAUTH2_CLIENT_ID'),
    client_secret=os.environ.get('OAUTH2_CLIENT_SECRET'),
    authorize_url='https://hemis.tersu.uz/oauth/authorize',
    access_token_url='https://hemis.tersu.uz/oauth/access-token',
)


def hemis_login_teacher(request):
    redirect_uri = request.build_absolute_uri(reverse('users:auth'))
    return oauth.teacher.authorize_redirect(request, redirect_uri)


def auth(request):
    token = oauth.teacher.authorize_access_token(request)
    user_info_url = "https://hemis.tersu.uz/oauth/api/user"
    headers = {'Authorization': f'Bearer {token["access_token"]}'}
    response = requests.get(user_info_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        employee_id_number = data['employee_id_number']
        print(AllowedTeachers.objects.filter(teacher__employee_id_number=employee_id_number))

        if AllowedTeachers.objects.filter(teacher__employee_id_number=employee_id_number).exists():
            is_voter = AllowedTeachers.objects.get(teacher__employee_id_number=employee_id_number)
            if CustomUser.objects.filter(hemis_id=employee_id_number).exists():
                user = CustomUser.objects.get(hemis_id=employee_id_number)
                if user is not None:
                    login(request, user)
                    if is_voter.voter:
                        return redirect('teachers:webapp')
                    else:
                        return redirect('teachers:table_result')
                else:
                    return JsonResponse({'error': 'HEMIS orqali kirishda xatolik. Xatolik kodi: 500'})
            else:
                uuid = data['uuid']
                employee_id = data['employee_id']
                roles = data['roles']
                short_name = data['name']
                user_login = data['login']
                email = data['email']
                picture = data['picture']
                first_name = data['firstname']
                last_name = data['surname']
                third_name = data['patronymic']
                phone = data['phone']
                user = CustomUser.objects.create(
                    username=user_login,
                    email=email,
                    hemis_id=employee_id_number,
                    id_number=employee_id,
                    first_name=first_name,
                    last_name=last_name,
                    picture=picture,
                    short_name=short_name,
                    full_name=f"{short_name} {third_name}",
                    third_name=third_name,
                    roles=roles,
                    active_role=roles[0]['name'],
                    phone=phone,
                    uuid=uuid,
                )
                user.set_password(employee_id_number)
                user.save()

                if user is not None:
                    login(request, user)
                    if is_voter.voter:
                        return redirect('teachers:webapp')
                    else:
                        return redirect('teachers:table_result')
                else:
                    return JsonResponse({'error': 'HEMIS orqali kirishda xatolik. Xatolik kodi: 500'})
        else:
            return render(request, 'allowance.html')
    else:
        return JsonResponse({"error": f"HEMIS orqali kirishda xatolik. Xatolik kodi: {response.status_code}"})


class LoginView(View):
    def get(self, request):
        return redirect('users:hemis_login_teacher')


def logout(request):
    request.session.flush()
    return redirect('https://hemis.tersu.uz/dashboard/logout')