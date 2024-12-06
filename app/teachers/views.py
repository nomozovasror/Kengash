import os
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from django.http import JsonResponse, HttpResponse
import json
from .models import *

BOT_TOKEN = os.environ.get('BOT_TOKEN')


def clear_all_employee_departments():
    employees = Employee.objects.all()

    for employee in employees:
        employee.department.clear()
    print(f"Xodimlar uchun bo'llimlar tozalandi.")


@login_required()
@transaction.atomic()
def update_and_save_employee(request):
    token = os.environ.get('HEMIS_TOKEN')
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = 'https://student.tersu.uz/rest/v1/data/employee-list'

    get_page_count_params = {
        'type': 'all',
        'page': 1,
        'limit': 100
    }

    get_page_count_response = requests.get(url, headers=headers, params=get_page_count_params)
    if get_page_count_response.status_code == 200:
        clear_all_employee_departments()
        page_count = get_page_count_response.json()['data']['pagination']['pageCount']
        employees = Employee.objects.filter(is_archive=False)

        employee_api_ids = []
        employee_database_ids = [x.employee_id_number for x in employees]

        for page in range(1, page_count + 1):
            params = {
                'type': 'all',
                'page': page,
                'limit': 100
            }
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                items = response.json()['data']['items']
                for item in items:
                    try:
                        employee_api_ids.append(item['employee_id_number'])
                        gender, _ = Gender.objects.get_or_create(code=item['gender']['code'],
                                                                 defaults={'name': item['gender']['name']})

                        academic_degree, _ = AcademicDegree.objects.get_or_create(
                            code=item['academicDegree']['code'],
                            defaults={'name': item['academicDegree']['name']}
                        )

                        academic_rank, _ = AcademicRank.objects.get_or_create(
                            code=item['academicRank']['code'],
                            defaults={'name': item['academicRank']['name']}
                        )

                        structure_type, _ = StructureType.objects.get_or_create(
                            code=item['department']['structureType']['code'],
                            defaults={'name': item['department']['structureType']['name']}
                        )

                        locality_type, _ = LocalityType.objects.get_or_create(
                            code=item['department']['localityType']['code'],
                            defaults={'name': item['department']['localityType']['name']}
                        )

                        employment_form, _ = EmploymentForm.objects.get_or_create(
                            code=item['employmentForm']['code'],
                            defaults={'name': item['employmentForm']['name']}
                        )

                        employment_staff, _ = EmploymentStaff.objects.get_or_create(
                            code=item['employmentStaff']['code'],
                            defaults={'name': item['employmentStaff']['name']}
                        )

                        staff_position, _ = StaffPosition.objects.get_or_create(
                            code=item['staffPosition']['code'],
                            defaults={'name': item['staffPosition']['name']}
                        )

                        employee_status, _ = EmployeeStatus.objects.get_or_create(
                            code=item['employeeStatus']['code'],
                            defaults={'name': item['employeeStatus']['name']}
                        )

                        employee_type, _ = EmployeeType.objects.get_or_create(
                            code=item['employeeType']['code'],
                            defaults={'name': item['employeeType']['name']}
                        )

                        department, _ = Department.objects.get_or_create(
                            id=item['department']['id'],
                            defaults={
                                'name': item['department']['name'],
                                'code': item['department']['code'],
                                'structure_type': structure_type,
                                'locality_type': locality_type,
                                'parent': item['department']['parent'],
                            }
                        )

                        department_branch, _ = DepartmentBranch.objects.get_or_create(
                            department=department,
                            employee_form=employment_form,
                            employee_staff= employment_staff,
                            employee_position= staff_position,
                            employee_status= employee_status,
                            employee_type=employee_type,
                        )

                        employee, created = Employee.objects.update_or_create(
                            employee_id_number=item['employee_id_number'],
                            defaults={
                                'meta_id': item['meta_id'],
                                'full_name': item['full_name'],
                                'short_name': item['short_name'],
                                'first_name': item['first_name'],
                                'second_name': item['second_name'],
                                'third_name': item['third_name'],
                                'gender': gender,
                                'birth_timestamp': item['birth_date'],
                                'image': item['image'],
                                'year_of_enter': item['year_of_enter'],
                                'specialty': item['specialty'],
                                'academicDegree': academic_degree,
                                'academicRank': academic_rank,
                                'decree_number': item['decree_number'],
                                'contract_date': item['contract_date'],
                                'created_at': item['created_at'],
                                'updated_at': item['updated_at'],
                                'hash': item['hash'],
                                'is_archive': False
                            }
                        )
                        employee.department.add(department_branch)
                    except Exception as e:
                        print(e)
                        return HttpResponse(e)
            else:
                print(response.status_code)
                return redirect('teachers:webapp')

        employee_api_ids = list(dict.fromkeys(employee_api_ids))

        fired_employees = list(set(employee_database_ids) - set(employee_api_ids))
        if fired_employees:
            for employee in fired_employees:
                try:
                    fired = Employee.objects.get(employee_id_number=employee)
                    fired.is_archive = True
                    fired.save()
                except Exception as e:
                    messages.warning(request, e)

        messages.success(request, 'muvaffaqiyatli saqlandi')
        return redirect('teachers:webapp')

    else:
        messages.error(request, f"get page count error. status code {get_page_count_response.status_code}")
        return redirect('teachers:webapp')


@login_required()
def webapp_view(request):
    return render(request, 'index.html')


