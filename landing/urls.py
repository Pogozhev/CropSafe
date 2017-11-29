
from django.conf.urls import url
from landing import views

urlpatterns = [
    url(r'^$', views.landing,name='land'),
    url(r'^dashboard/', views.dashboard,name='dashboard'),
]
