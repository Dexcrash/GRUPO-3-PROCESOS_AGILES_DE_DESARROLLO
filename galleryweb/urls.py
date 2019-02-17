from django.conf.urls import url
from . import views
from django.urls import path, include # new


urlpatterns = [
    url(r'add$', views.add_image, name='addImage'),
    url(r'^$', views.galeria, name='list'),
    url(r'^edit_user$', views.edit_user, name='editUser'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^detalle(?P<media_id>\d+)/$', views.media_detail, name='media_detail'),
    url(r'^login$', views.loginview, name='login'),
    url('accounts', include('django.contrib.auth.urls')),  # new
    url(r'^clips$', views.clips, name='clips'),
    url(r'^get_user_by_id$', views.get_user_by_id, name='user_by_id'),

]
