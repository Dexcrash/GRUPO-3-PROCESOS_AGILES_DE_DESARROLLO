from django.conf.urls import url
from . import views
from django.urls import path, include # new


urlpatterns = [
    url(r'^$', views.galeria, name='list'),
    url(r'^edit_user$', views.edit_user, name='editUser'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login$', views.loginview, name='login'),
    url('accounts', include('django.contrib.auth.urls')),  # new
    url(r'^clips$', views.clips, name='clips'),
    url(r'^get_user_by_id$', views.get_user_by_id, name='user_by_id'),
    url(r'^logOut', views.logOut, name='logOut'),
    url(r'^authenticated', views.authenticate, name='autho'),
    url(r'^multimedias_by_user', views.multimedias_by_user, name='multimedias_by_user'),
]
