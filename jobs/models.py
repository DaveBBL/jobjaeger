from django.db import models


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
    company = models.ForeignKey("Company", on_delete=models.CASCADE)


class Interview(models.Model):
    interview_date = models.DateTimeField()
    interview_notes = models.TextField(blank=True)
    role = models.ForeignKey("Role", on_delete=models.CASCADE)