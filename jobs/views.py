import pyecharts as pe
from django.shortcuts import render
from django.template import loader
from pyecharts.constants import DEFAULT_HOST
from jobs.models import JobsInfo
from django.http import HttpResponse

from jobs.process_data.jobs_data_init import process_field
from jobs.process_data.jobs_data_init import process_reqirement


def home(request):
    return render(request, 'jobs/home.html')


def echarts(request):
    return render(request, 'jobs/echarts.html')


def blog(request):
    return render(request, 'jobs/blog.html')


def contact(request):
    return render(request, "jobs/contact.html", {"content": ["welcome to contact page", "my email is vickey557@gmail.com"]})


def create_bar():
    # query with django models objects
    user_list = JobsInfo.objects.all().values_list("job_title", "job_salary", "job_exp")
    # query with pymysql
    page = pe.Page()
    salary = process_field("job_salary")
    requirement = process_reqirement("job_requirement")
    x1, x2, x3, y1, y2, y3 = [], [], [], [], [], []
    sal_min = salary[0]
    sal_avg = salary[1]
    for s1 in sal_min:
        x1.append(s1[0])
        y1.append(s1[1])
    for s2 in sal_avg:
        x2.append(s2[0])
        y2.append(s2[1])
    for s3 in requirement:
        x3.append(s3[0])
        y3.append(s3[1])
    name1 = ["sal_min"]
    name2 = ["sal_avg"]
    name3 = ["sal_req"]
    # bar
    bar = pe.Bar("my first Chart", "subtitle", width=900, height=300)
    bar.add(name1, x1, y1)
    bar.add(name2, x2, y2)
    page.add(bar)
    # line
    line = pe.Line('my first Line', "subtitle", width=900, height=300)
    line.add(name1, x1, y1)
    line.add(name2, x2, y2)
    page.add(line)
    # pie

    pie = pe.Pie("requirement", "subtitle", width=900, height=1200)
    pie.add(name3, x3, y3)
    page.add(pie)
    return page


def py_eharts(request):
    template = loader.get_template('jobs/pyecharts.html')
    page = create_bar()
    context = dict(
        myechart=page.render_embed(),
        host=DEFAULT_HOST,
        script_list=page.get_js_dependencies(),
    )
    return HttpResponse(template.render(context, request))
