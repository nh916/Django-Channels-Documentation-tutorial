# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('user connected')

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        print('user disconnected')

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print('message received')

        text_data_json = json.loads(text_data)
        event = text_data_json['event']
        message = text_data_json['message']

        if event == 'handler_1':
            await self.handler_1(message)
        elif event == 'handler_2':
            await self.handler_2(message)
        elif event == 'handler_3':
            await self.handler_3(message)

    async def handler_1(self, message):
        print('Handling "handler_1" event')
        print(message)
        # Process the message for "handler_1" event

    async def handler_2(self, message):
        print('Handling "handler_2" event')
        print(message)
        # Process the message for "handler_2" event

    async def handler_3(self, message):
        print('Handling "handler_3" event')
        print(message)
        # Process the message for "handler_3" event
