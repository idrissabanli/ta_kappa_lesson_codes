import json
from config.extentions import RedisConfig

class Publish(RedisConfig):

    def __init__(self, data, event_type):
        self.data = data
        self.event_type = event_type
        self.send()

    def send(self):
        message = self.stringfy()
        self.client.publish(self.CHANNEL_NAME, message=message)

    def stringfy(self):
        return json.dumps({
            'data': self.data,
            'event_type': self.event_type
        })