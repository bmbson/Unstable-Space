from django.urls import path
from . import views

urlpatterns = [
    # ex: '/'
    path('mixadmin', views.mixadminfront, name='mixadminfront'),  
    path('createmix', views.createmix, name='createmix'),
    path('deletemix', views.deletemix, name='deletemix'),
    path('updatemix', views.updatemix, name='updatemix'),
]