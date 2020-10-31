from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path


application = ProtocolTypeRouter(
    {"websocket": AllowedHostsOriginValidator(URLRouter([]))}
)
