import redis

class RedisConfig:
    channel_name = 'events'

    @property
    def client(self):
        return redis.Redis(host='localhost', port=6379, db=0)


class EmailConfig:
    EMAIL_HOST_USER = 'dadashbeyli93@gmail.com'
    EMAIL_HOST_PASSWORD = 'eibavvquuowmcuov'