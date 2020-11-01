from django.shortcuts import render
from django.conf import settings

from chat.models import Message


def chat_view(request):
    if request.method == "POST":
        if "username" in request.POST:
            username = request.POST["username"]
            request.session["username"] = username
            messages = Message.objects.all()
            return render(
                request,
                "chat.html",
                {
                    "ws_url": settings.WESBSOCKET_URL,
                    "username": username,
                    "messages": messages,
                }
            )

    if request.session.get("username", None):
        username = request.session["username"]
        messages = Message.objects.all()
        return render(
            request,
            "chat.html",
            {
                "ws_url": settings.WESBSOCKET_URL,
                "username": username,
                "messages": messages,
            }
        )
    else:
        return render(request, "input.html")

