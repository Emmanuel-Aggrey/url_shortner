from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # methods

    path('', views.LinkCreate.as_view(), name='home'),
    # path('<int:pk>/', views.LinkShow.as_view(), name='link_show'),
    path('detail/<int:pk>/',views.detailpage,name='detailpage'),
    path('<str:short_url>/',
         views.RedirectToLongURL.as_view(), name='redirect_short_url'),

    path('api/<int:pk>/',views.ShortUrlApi.as_view()),
    path('api/<str:hash_id>/',views.ShortToLongUrlSerializer.as_view()),

]
