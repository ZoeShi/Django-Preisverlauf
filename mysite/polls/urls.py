from django.conf.urls import url

from . import views



app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/product/$', views.ProductView.as_view(), name='product'),
    url(r'^(?P<pk>[0-9]+)/product/csv$', views.ProductCSVView.as_view(), name='csv'),
    url(r'dateiimport$', views.UploadView.as_view(), name='upload'),
    url(r'^search/$', views.search.as_view(), name='search')
]
