import pyecharts as pe
from django.shortcuts import render
from django.template import loader
from pyecharts.constants import DEFAULT_HOST
from jobs.models import JobsInfo
from django.http import HttpResponse

def echarts(request):
    return render(request, 'jobs/echarts.html')


def create_bar():
    user_list = JobsInfo.objects.all().values_list("job_title", "job_salary", "job_exp")
    page = pe.Page()

    name = ["服装"]
    name2 = ["电器"]
    x = list(user_list[0])
    y = ["50", 200, 100]
    y2 = ["50", 300, 1400]
    # bar
    bar = pe.Bar("我的第一个图表", "这里是副标题", width=600, height=300)
    bar.add(name, x, y)
    bar.add(name2, x, y2)
    page.add(bar)
    # line
    line = pe.Line('Demo Line', "这里是副标题", width=600, height=300)
    line.add(name, x, y)
    line.add(name2, x, y2)
    page.add(line)
    return page


def py_eharts(request):
    template = loader.get_template('jobs/pyecharts.html')
    page = create_bar()
    context = dict(
        myechart=page.render_embed(),
        host=DEFAULT_HOST,
        script_list=page.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))
