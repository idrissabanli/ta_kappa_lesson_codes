from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin



class BlackListIPMiddleware(MiddlewareMixin):
    BLACK_IP_LIST = [
        # '10.10.80.69',
        # '10.10.80.105'
    ]

    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))
        if request.META.get('REMOTE_ADDR') in self.BLACK_IP_LIST:
            return HttpResponseForbidden()
