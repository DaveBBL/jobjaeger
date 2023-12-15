# Generated by Django 5.0 on 2023-12-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_interview_role_role_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='interview_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='job_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
