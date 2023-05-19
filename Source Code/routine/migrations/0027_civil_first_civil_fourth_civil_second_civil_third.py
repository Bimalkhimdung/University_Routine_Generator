# Generated by Django 4.1.3 on 2022-11-15 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0026_auto_20220307_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Civil_First',
            fields=[
                ('batch', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
                ('Lecturer_Name', models.CharField(blank=True, default=None, max_length=50)),
                ('Lecturer_Code', models.SlugField(max_length=10)),
                ('Lecturer_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Lecturer_Subject', models.CharField(blank=True, default=None, max_length=100)),
                ('Lecturer_Period', models.IntegerField(blank=True, default=0, null=True)),
                ('Lab_Class', models.CharField(blank=True, default=None, max_length=50)),
                ('Lab_Subject', models.CharField(blank=True, default=None, max_length=50)),
                ('Lab_Lec_Period', models.CharField(blank=True, default=0, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Civil_Fourth',
            fields=[
                ('batch', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
                ('Lecturer_Name', models.CharField(blank=True, default=None, max_length=50)),
                ('Lecturer_Code', models.SlugField(max_length=10)),
                ('Lecturer_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Lecturer_Subject', models.CharField(blank=True, default=None, max_length=100)),
                ('Lecturer_Period', models.IntegerField(blank=True, default=0, null=True)),
                ('Lab_Class', models.CharField(blank=True, default=None, max_length=50)),
                ('Lab_Subject', models.CharField(blank=True, default=None, max_length=50)),
                ('Lab_Lec_Period', models.CharField(blank=True, default=0, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Civil_Second',
            fields=[
                ('batch', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
                ('Lecturer_Name', models.CharField(blank=True, default=None, max_length=50)),
                ('Lecturer_Code', models.SlugField(max_length=10)),
                ('Lecturer_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Lecturer_Subject', models.CharField(blank=True, default=None, max_length=100)),
                ('Lecturer_Period', models.IntegerField(blank=True, default=0, null=True)),
                ('Lab_Class', models.CharField(blank=True, default=None, max_length=50)),
                ('Lab_Subject', models.CharField(blank=True, default=None, max_length=50)),
                ('Lab_Lec_Period', models.CharField(blank=True, default=0, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Civil_Third',
            fields=[
                ('batch', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
                ('Lecturer_Name', models.CharField(blank=True, default=None, max_length=50)),
                ('Lecturer_Code', models.SlugField(max_length=10)),
                ('Lecturer_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Lecturer_Subject', models.CharField(blank=True, default=None, max_length=100)),
                ('Lecturer_Period', models.IntegerField(blank=True, default=0, null=True)),
                ('Lab_Class', models.CharField(blank=True, default=None, max_length=50)),
                ('Lab_Subject', models.CharField(blank=True, default=None, max_length=50)),
                ('Lab_Lec_Period', models.CharField(blank=True, default=0, max_length=20, null=True)),
            ],
        ),
    ]
