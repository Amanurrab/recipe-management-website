print("🔥 Middleware Loaded")

class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Middleware called")
        response = self.get_response(request)
        return response