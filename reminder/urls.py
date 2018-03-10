from django.conf.urls import url
from reminder import views

app_name = 'reminder'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logs/$', views.logs, name='logs'),
]