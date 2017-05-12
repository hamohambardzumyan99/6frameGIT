from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^free$', views.free_all, name='free_all'),
    url(r'^paid$', views.paid_all, name='paid_all'),
    url(r'^free/(?P<id>\d+)', views.show_free, name='ID'),
    url(r'^paid/(?P<id>\d+)', views.show_paid, name='ID_paid'),

]
