from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # methods

    path('', views.LinkCreate.as_view(), name='home'),
    path('<int:pk>/', views.LinkShow.as_view(), name='link_show'),


    path('<str:short_url>/',
         views.RedirectToLongURL.as_view(), name='redirect_short_url'),

   
]
