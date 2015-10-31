from django.conf.urls import url
from application import views


urlpatterns = [

    url(r'^$', views.welcome),
    url(r'^contactme', views.Contact_Me_Form),
    url(r'^login_register', views.login_register_page),
    url(r'^register_page', views.register_page),
    url(r'^register', views.register),
]