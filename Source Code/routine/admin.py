from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Computer_First)
class Computer_FirstAdmin(admin.ModelAdmin):
    list_display = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

@admin.register(Computer_Second)
class Computer_SecondAdmin(admin.ModelAdmin):
    list_display = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

@admin.register(Computer_Third)
class Computer_ThirdAdmin(admin.ModelAdmin):
    list_display = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

@admin.register(Computer_Fourth)
class Computer_FourthAdmin(admin.ModelAdmin):
    list_display = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']


@admin.register(Electrical_First)
class Electrical_FirstAdmin(admin.ModelAdmin):
    list_display = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

@admin.register(Electrical_Second)
class Electrical_SecondAdmin(admin.ModelAdmin):
    list_display = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']   

@admin.register(Electrical_Third)
class Electrical_ThirdAdmin(admin.ModelAdmin):
    list_display = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

@admin.register(Electrical_Fourth)
class Electrical_FourthAdmin(admin.ModelAdmin):
    list_display = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']


@admin.register(Labroom)
class LabroomAdmin(admin.ModelAdmin):
    list_display = ['Lab_Name', 'Lab_No']