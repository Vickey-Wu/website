from django.db import models
from django.contrib import admin
class JobsInfo(models.Model):
    job_title = models.CharField(max_length=30)
    job_salary = models.CharField(max_length=30)
    job_requirement = models.TextField()
    job_addr = models.CharField(max_length=100)
    job_exp = models.CharField(max_length=20)
    job_edu = models.CharField(max_length=20)
    job_tags = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_employee_num = models.CharField(max_length=20)
    company_type = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "jobs info"
