# Generated by Django 3.1.3 on 2022-02-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0020_auto_20220215_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_first',
            name='Lab_Class',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='computer_first',
            name='Lab_Period',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
    ]
