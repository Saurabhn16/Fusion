# Generated by Django 3.1.5 on 2024-02-19 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_management', '0008_studentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='hall_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]