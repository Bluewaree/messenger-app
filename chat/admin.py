from django.contrib import admin

from chat.models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "message",
        "username"
    )

admin.site.register(Message, MessageAdmin)
