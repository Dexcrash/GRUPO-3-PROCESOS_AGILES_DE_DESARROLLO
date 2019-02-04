from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'add/$', views.add_image, name='addImage'),
    url(r'^$', views.galeria, name='list'),
]