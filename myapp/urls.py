from django.urls import path

from .views import main_page, channel_page

urlpatterns = [
  path('', main_page, name='main_page'),
  path('<str:name>/', channel_page, name='channel_page'),
]