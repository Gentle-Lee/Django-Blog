from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.homepage,name = 'homepage'),
    url(r'article_list$', views.article_list, name='article_list'),
    url(r'programming$', views.programming_list, name='programming_list'),
    url(r'Jotting$', views.jotting_list, name='jotting_list'),
    url(r'article/(?P<article_id>\d+)$',views.article_detail,name = 'article_detail'),
    url(r'^search/$', views.search, name='search'),
]