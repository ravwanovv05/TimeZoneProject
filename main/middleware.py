from django.http import HttpResponseForbidden, JsonResponse
from django.views import View


class IPRestrictedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        client_ip = request.META.get('REMOTE_ADDR')
        ip_address = [
            '127.0.0.1',
            '10.10.3.108 '
        ]
        if client_ip not in ip_address and request.path.find('admin') != -1:
            return HttpResponseForbidden('Permission denied!')
        response = self.get_response(request)
        return response


# First API
class HelloAPIView(View):
    def get(self, request):
        return JsonResponse({'success': True, 'message': 'Hello World!'})






