from django.conf.urls import url
from django.contrib import admin
from jobs import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^echarts/', views.echarts, name='echarts'),
]
