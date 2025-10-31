from django.urls import path
from .views import message

urlpatterns = [
#     path('display/', display, name='display'),
#     path('myview/', my_view, name='myview'),
    path('message/', message, name='message'),
]