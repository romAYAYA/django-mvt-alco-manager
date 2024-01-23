from django.http import HttpRequest


class AllowAllOriginsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        with open('logs.txt', 'a', encoding='utf-8') as f:
            f.write(f'{request.path}: {request.user.username}\n')

        return response
