# Generated by Django 3.1.3 on 2022-02-12 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('batch', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
                ('Lecturer_Name', models.CharField(max_length=50)),
                ('Lecturer_Code', models.SlugField(max_length=10)),
                ('Lecturer_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Lecturer_Subject', models.CharField(max_length=100)),
                ('Lecturer_Period', models.IntegerField()),
                ('Lab_Class', models.CharField(max_length=10)),
                ('Lab_Period', models.IntegerField()),
            ],
        ),
    ]
