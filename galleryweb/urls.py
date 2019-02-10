from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'add/$', views.add_image, name='addImage'),
    url(r'^$', views.galeria, name='list'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^detalle/(?P<media_id>\d+)/$', views.media_list, name='media_list'),
]
