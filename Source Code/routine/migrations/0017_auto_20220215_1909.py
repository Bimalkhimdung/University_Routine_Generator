# Generated by Django 3.1.3 on 2022-02-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0016_auto_20220215_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_first',
            name='Lab_Period',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
