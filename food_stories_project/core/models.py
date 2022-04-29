from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=50)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    # def serializer(self):
    #     return {
    #         'full_name': self.full_name,
    #         'email': self.email,
    #         'subject': self.subject,
    #         'message': self.message,
    #         'created_at': self.created_at
    #     }

