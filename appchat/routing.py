from django.urls import re_path
from . import consumers
from django.urls import path

# URLs that handle the WebSocket connection are placed here.
websocket_urlpatterns = [
    #    re_path(r"ws/appchat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    path('ws/appchat/<room_name>/', consumers.ChatConsumer.as_asgi()),
]
