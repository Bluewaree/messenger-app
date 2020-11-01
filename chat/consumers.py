from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from chat.models import Message


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add(
            "chat",
            self.channel_name
        )
        await self.accept()

    async def receive_json(self, content, **kwargs):
        response = await self.get_response(content)
        await self.channel_layer.group_send(
            "chat",
            {
                "type": "send_message",
                "data": response
            }
        )

    async def get_response(self, content):
        message = content["message"]
        username = content["username"]
        await self.create_message_instance(message, username)
        return {
            "message": message,
            "username": username
        }

    async def send_message(self, event):
        await self.send_json({
            "type": "chat.send",
            "data": event["data"]
        })

    @database_sync_to_async
    def create_message_instance(self, message, username):
        Message.objects.create(message=message, username=username)
