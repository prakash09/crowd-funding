from django.conf.urls import patterns, include, url

urlpatterns = patterns('transaction_app.views',
    url(r'^index/$', 'home', {'cat_name': 'home'},name='dashboard'),
    url(r'^category/(?P<cat_name>\w+)/$', 'home', name='category'),
    url(r'^article/(?P<article_id>[\w\-]+)/$', 'article', name='article'),
    url(r'^investment/(?P<slug>[\w\-]+)/$', 'investments', name='investment'),
    url(r'^about/$', 'about',name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^search/$', 'blog_search', name='blog_search'),
    url(r'^ckeditor/', include('ckeditor.urls')),
)
