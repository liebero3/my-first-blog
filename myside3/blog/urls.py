from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^blog\/$', views.post_list, name='post_list'),
    url(r'^blog8a\/$', views.post_list8a, name='post_list8a'),
    url(r'^blog8b\/$', views.post_list8b, name='post_list8b'),
    url(r'^blog9c\/$', views.post_list9c, name='post_list9c'),
    url(r'^$', views.show_homepage, name='index'),
    url(r'^blog/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^login/$', views.login_user, name='log_in'),
    url(r'^blog/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^change_password_done/$', views.change_password_done, name='change_password_done'),
]
