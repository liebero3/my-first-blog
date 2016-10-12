from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog\/$', views.post_list, name='post_list'),
    url(r'^$', views.show_homepage, name='index'),
    url(r'^index\/$', views.show_homepage, name='index'),
]
