from django.urls import path
from . import views

urlpatterns = [
    # ex: '/'
    path('', views.frontPage, name='frontpage'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('secret', views.secret, name='secret'),
    path('mixes', views.mixes, name='mixes'),
    path('about', views.about, name='about'),
    path('merch', views.merch, name='merch'),
    path('blog', views.blog, name='blog'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy')
] 