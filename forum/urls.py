from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<slug:category_slug>/',
         views.thread_list, name='thread_list'),
    path('category/<slug:category_slug>/thread/<slug:thread_slug>/',
         views.thread_detail, name='thread_detail'),
    path('category/<slug:category_slug>/new_thread/',
         views.new_thread, name='new_thread'),
    path('category/<slug:category_slug>/thread/<slug:thread_slug>/new_post/',
         views.new_post, name='new_post'),
]