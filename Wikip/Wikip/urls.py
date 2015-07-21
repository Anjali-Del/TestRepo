"""Wikip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from wikipage import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homepage/$', views.homepage),
    url(r'^signup/$', views.signup),
    url(r'^login/$', views.login),
    url(r'^login_view/$', views.login_view),
    url(r'^new_session/$', views.new_session),
    url(r'^add_view/$', views.add_view),
    url(r'^logout/$', views.logout),
    url(r'^view_article/$', views.view_article),
    url(r'^new_article/$', views.new_article),
    url(r'^success_page/$', views.success_page),
    url(r'^delete_article/(\d+)/$', views.delete_article), 
    url(r'^edit_article/(\d+)/$', views.edit_article), 
    url(r'^success_edit/(\d+)/$', views.success_edit), 
]
