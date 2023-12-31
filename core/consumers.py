import json
from channels.generic.websocket import AsyncWebsocketConsumer
class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = 1
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        await self.send(text_data=json.dumps({"message": "connection sucessfull....."}))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print("tex_data_json---------", text_data_json)
            
            
    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=message)