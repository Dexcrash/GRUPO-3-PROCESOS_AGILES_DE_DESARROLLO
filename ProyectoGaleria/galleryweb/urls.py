from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.galeria, name='index'),
    url(r'list', views.galeria, name='list'),
    url(r'add/$', views.add_image, name='addImage'),
]