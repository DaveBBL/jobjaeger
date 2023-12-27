from django.db import models
from django.db.models.functions import Now


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    url = models.CharField(null=True, blank=True, max_length=200)
    notes = models.TextField(null=True, blank=True)


class Role(models.Model):
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)
    job_notes = models.TextField(null=True, blank=True)
    responsibilities = models.TextField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Application(models.Model):
    apply_date = models.DateField(default=Now())
    apply_notes = models.TextField(null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    # contact = models.ForeignKey(Contact, on_delete=models.CASCADE)


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=50)
    contact_email = models.EmailField(null=True)
    contact_phone = models.IntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Interview(models.Model):
    interview_date = models.DateTimeField()
    interview_notes = models.TextField(blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_start_date = models.DateTimeField(null=True, blank=True)
    task_due_date = models.DateTimeField(null=True, blank=True)
    task_complete = models.BooleanField(default=False)
    task_notes = models.TextField(null=True, blank=True)

    