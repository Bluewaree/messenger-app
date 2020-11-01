import pytest
from channels.db import database_sync_to_async
from channels.testing import WebsocketCommunicator
import asyncio
from config.routing import application
from channels.layers import get_channel_layer

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

    @pytest.mark.django_db
    @pytest.mark.asyncio
    async def test_chat_process(self, settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        channel_layer = get_channel_layer()

        self.communicators = []
        self.communicators.append(await self.auth_connect("communicator1", "chat/"))
        self.communicators.append(await self.auth_connect("communicator2", "chat/"))
        await self.communicators[0].send_json_to({"message": "Hello", "username": "communicator1"})

        for communicator in self.communicators:
            response = await communicator.receive_json_from()
            assert response["data"]["message"] == "Hello"
            assert response["data"]["username"] == "communicator1"
            await communicator.disconnect()
