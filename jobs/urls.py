from django.conf.urls import url
from django.contrib import admin
from jobs import views

urlpatterns = [
    # url(r'^admin', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^echarts$', views.echarts, name='echarts'),
    url(r'^pyecharts$', views.py_eharts, name='pyecharts'),
]
