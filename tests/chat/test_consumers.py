import pytest
from channels.db import database_sync_to_async
from channels.testing import WebsocketCommunicator
import asyncio
from config.routing import application
from channels.layers import get_channel_layer

from chat.models import Message

TEST_CHANNEL_LAYERS = {
    "default": {"BACKEND": "channels.layers.InMemoryChannelLayer",},
}


class TestChatConsumer:

    async def auth_connect(self, username, path):
        communicator = WebsocketCommunicator(
            application=application, path=f'{path}?username=username',
        )

        connected, _ = await communicator.connect()
        assert connected is True
        return communicator

    @database_sync_to_async
    def check_message_objects_count(self, count):
        assert Message.objects.count() == count

    @database_sync_to_async
    def check_message_object_fields(self):
        message = Message.objects.last()
        assert message.message == self.message
        assert message.message == self.username

    @pytest.mark.django_db
    @pytest.mark.asyncio
    async def test_chat_process(self, settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        channel_layer = get_channel_layer(0)

        messages = await self.check_message_objects_count(0)
        self.communicators = []
        self.communicators.append(await self.auth_connect("communicator1", "chat/"))
        self.communicators.append(await self.auth_connect("communicator2", "chat/"))
        self.message = "Hello"
        self.username = "communicator1"
        await self.communicators[0].send_json_to({"message": self.message, "username": self.username})
        messages = await self.check_message_objects_count(1)
        messages = await self.check_message_object_fields()

        for communicator in self.communicators:
            response = await communicator.receive_json_from()
            assert response["data"]["message"] == "Hello"
            assert response["data"]["username"] == "communicator1"
            await communicator.disconnect()
