from django.conf.urls import patterns, include, url

urlpatterns = patterns('transaction_app.views',
    url(r'^dashboard/$', 'dashboard',name='dashboard'),
    url(r'^index/$', 'home', {'cat_name': 'home'},name='home_page'),
    url(r'^category/(?P<cat_name>\w+)/$', 'home', name='category'),
    url(r'^investment/(?P<slug>[\w\-]+)/$', 'investments', name='investment'),
    url(r'^search/$', 'blog_search', name='blog_search'),
    url(r'^ckeditor/', include('ckeditor.urls')),
)
