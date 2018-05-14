from django.conf.urls import url
from django.contrib import admin
from . import views

# views.py에서 만든 내용 (index, detail, about)
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.detail, name='index'),
    # url(r'^$', views.about, name='index'),

]
