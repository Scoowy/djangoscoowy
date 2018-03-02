from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.lista_post, name='lista_post'),
    url(r'^blog/post/(?P<pk>[0-9]+)/$', views.post_completo, name='post_completo'),
    url(r'^contactanos/$', views.contactanos, name='contactanos'),
    url(r'^contactanos/gracias/$', views.contactanos_gracias,
        name='contactanos_gracias'),
    url(r'^buscar/$', views.buscar, name='buscar'),
]
