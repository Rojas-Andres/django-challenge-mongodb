from django.db import connection


class KeepMongoConnectionAliveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            connection.ensure_connection()
        except Exception as e:
            print(f"Reconectando a MongoDB: {e}")
        response = self.get_response(request)
        return response
