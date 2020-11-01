from django.shortcuts import render
from django.conf import settings


def chat_view(request):
    return render(request, "chat.html", {"ws_url": settings.WESBSOCKET_URL})
