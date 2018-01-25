from django.contrib import admin
from jobs import models

class JobsInfoCustomize(admin.ModelAdmin):
    list_display = ('job_title','job_salary','job_requirement','job_addr','job_exp','job_edu','job_tags','company_name','company_employee_num','company_type')
    # list_editable = ('job_title')
    # search_fields = ('job_title')
    list_filter = ('job_title','job_salary')

admin.site.register(models.JobsInfo, models.JobsInfoCustomize)