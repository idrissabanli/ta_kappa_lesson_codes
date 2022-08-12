import json

from core.config import RedisConfig
from core.send_mail import SendMail


class Handler:
    event_type = 'send_mail'

    def __init__(self):
        redis_conf = RedisConfig()
        self.redisclient = redis_conf.client
        p = self.redisclient.pubsub()
        p.psubscribe(**{redis_conf.channel_name:self.handle})
        p.run_in_thread()

    def handle(self, event):
        self.data = event.pop('data')
        message = self.to_dict()
        if message['event_type'] == self.event_type:
            SendMail(**message['data'])
            print('sent')

    def to_dict(self):
        return json.loads(self.data)

    