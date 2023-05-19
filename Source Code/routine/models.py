from django.db import models


class Computer_First(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(blank = True, null=True, default=0)
    Lab_Class = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Subject = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Lec_Period = models.CharField(max_length = 20, blank =True, null=True, default=0)

    def __str__(self):
        return self .Lecturer_Name

class Computer_Second(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(blank = True, null=True, default=0)
    Lab_Class = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Subject = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Lec_Period = models.CharField(max_length = 20, blank =True, null=True, default=0)

    def __str__(self):
        return self .Lecturer_Name

class Computer_Third(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(blank = True, null=True, default=0)
    Lab_Class = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Subject = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Lec_Period = models.CharField(max_length = 20, blank =True, null=True, default=0)

    def __str__(self):
        return self .Lecturer_Name


class Computer_Fourth(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(blank = True, null=True, default=0)
    Lab_Class = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Subject = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Lec_Period = models.CharField(max_length = 20, blank =True, null=True, default=0)

    def __str__(self):
        return self .Lecturer_Name


class Electrical_First(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(blank = True, null=True, default=0)
    Lab_Class = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Subject = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Lec_Period = models.CharField(max_length = 20, blank =True, null=True, default=0)

    def __str__(self):
        return self .Lecturer_Name

class Electrical_Second(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(blank = True, null=True, default=0)
    Lab_Class = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Subject = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Lec_Period = models.CharField(max_length = 20, blank =True, null=True, default=0)

    def __str__(self):
        return self .Lecturer_Name
class Electrical_Third(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(blank = True, null=True, default=0)
    Lab_Class = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Subject = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Lec_Period = models.CharField(max_length = 20, blank =True, null=True, default=0)

    def __str__(self):
        return self .Lecturer_Name
class Electrical_Fourth(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(blank = True, null=True, default=0)
    Lab_Class = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Subject = models.CharField(max_length = 50, blank=True, default=None)
    Lab_Lec_Period = models.CharField(max_length = 20, blank =True, null=True, default=0)

    def __str__(self):
        return self .Lecturer_Name

class Labroom(models.Model):
    Lab_Name = models.CharField(max_length=50)
    Lab_No = models.IntegerField()

    def __str__(self):
        return self.Lab_Name
