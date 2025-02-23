from django.db import models

# Create your models here.
class Gender(models.Model):
    code = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name


class AcademicDegree(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class AcademicRank(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class StructureType(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class LocalityType(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    hemis_id = models.IntegerField()
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class EmploymentForm(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class EmploymentStaff(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class StaffPosition(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class EmployeeStatus(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class EmployeeType(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=50)
    structure_type = models.ForeignKey(StructureType, on_delete=models.CASCADE, null=True, blank=True)
    locality_type = models.ForeignKey(LocalityType, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class DepartmentBranch(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    employee_form = models.ForeignKey(EmploymentForm, on_delete=models.CASCADE, null=True, blank=True)
    employee_staff = models.ForeignKey(EmploymentStaff, on_delete=models.CASCADE, null=True, blank=True)
    employee_position = models.ForeignKey(StaffPosition, on_delete=models.CASCADE, null=True, blank=True)
    employee_status = models.ForeignKey(EmployeeStatus, on_delete=models.CASCADE, null=True, blank=True)
    employee_type = models.ForeignKey(EmployeeType, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.department} | {self.employee_staff} | {self.employee_position} | {self.employee_type}"


class Employee(models.Model):
    employee_id_number = models.CharField(max_length=150, unique=True)
    meta_id = models.IntegerField(null=True)
    hemis_id = models.IntegerField(unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=300)
    short_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150)
    third_name = models.CharField(max_length=150)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    birth_timestamp = models.BigIntegerField(null=True, blank=True)
    image = models.URLField(max_length=200)
    year_of_enter = models.IntegerField(null=True)
    specialty = models.CharField(max_length=500)
    academicDegree = models.ForeignKey(AcademicDegree, on_delete=models.PROTECT)
    academicRank = models.ForeignKey(AcademicRank, on_delete=models.PROTECT)
    department = models.ManyToManyField(DepartmentBranch)
    contract_number = models.CharField(max_length=100, null=True, blank=True)
    decree_number = models.CharField(max_length=100)
    contract_date = models.CharField(max_length=100)
    created_at = models.BigIntegerField(null=True)
    updated_at = models.BigIntegerField(null=True)
    hash = models.CharField(max_length=164)
    is_archive = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

class SelectedEmployee(models.Model):
    TYPE = (
        ('professor', 'Professor'),
        ('dotsent', 'Dotsent'),
        ('mudir', 'Mudir'),
        ('katta_oqituvchi', 'Katta O\'qituvchi'),
        ('oqituvchi_stajyor', 'O\'qituvchi-stajyor'),
        ('o\'qituvchi', 'O\'qituvchi'),

    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='selected_employee')
    type = models.CharField(max_length=20, choices=TYPE, null=True)
    which_position = models.CharField(max_length=255, null=True)
    created_at = models.DateField(null=True)

    def __str__(self):
        return self.employee.full_name


class Vote(models.Model):
    TYPE_CHOICE = (
        ('rozi', 'Roziman'),
        ('qarshi', 'Qarshiman'),
        ('betaraf', 'Betaraf')
    )
    employee = models.ForeignKey(SelectedEmployee, on_delete=models.CASCADE, related_name='votes')
    vote = models.CharField(max_length=20, choices=TYPE_CHOICE)
    session_id = models.UUIDField(null=True)

    def __str__(self):
        return f"{self.employee.employee.full_name}"