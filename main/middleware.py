from django.utils.deprecation import MiddlewareMixin


class SecurityHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response["X-Content-Type-Options"] = "nosniff"
        return response
