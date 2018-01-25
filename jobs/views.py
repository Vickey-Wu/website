from django.shortcuts import render

def echarts(request):
    return render(request, 'jobs/echarts.html')