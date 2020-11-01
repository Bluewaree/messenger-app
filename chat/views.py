from django.shortcuts import render
from django.conf import settings


def chat_view(request):
    if request.method == "POST":
        if "username" in request.POST:
            username = request.POST["username"]
            request.session["username"] = username
            return render(request, "chat.html", {"ws_url": settings.WESBSOCKET_URL, "username": username})

    if request.session.get("username", None):
        username = request.session["username"]
        return render(request, "chat.html", {"ws_url": settings.WESBSOCKET_URL, "username": username})
    else:
        return render(request, "input.html")

