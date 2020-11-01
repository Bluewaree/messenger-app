from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from chat.consumers import ChatConsumer


application = ProtocolTypeRouter(
    {"websocket": AllowedHostsOriginValidator(URLRouter([path("chat/", ChatConsumer),]))}
)
