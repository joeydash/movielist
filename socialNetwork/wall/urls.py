from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^users/(?P<user_name>[\w\-]+)/$', views.user_wall, name='user_wall'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^movie/$', views.movie, name='movie'),
    
]
