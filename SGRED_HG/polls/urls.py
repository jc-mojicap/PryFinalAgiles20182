from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^proyecto/$', views.proy, name='proy'),
    url(r'^recurso/$', views.addRecurso, name='addRecurso'),
    url(r'^artefacto/$', views.addArtefacto, name='addArtefacto'),
]