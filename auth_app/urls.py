from django.conf.urls import patterns, include, url

urlpatterns = patterns('auth_app.views',
    url(r'^$', 'landing_page', name = 'landing_page'),
    url(r'^sign-up/$', 'sign_up', name = 'sign_up'),
    url(r'^sign-in/$', 'sign_in', name = 'sign_in'),
    url(r'^sign-out/$', 'sign_out', name = 'sign_out'),
)
