# Generated by Django 3.1.6 on 2021-02-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200, null=True),
        ),
    ]
