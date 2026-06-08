from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HomeView(APIView):
    """
    Root endpoint for the Pulse Check API.
    """

    def get(self, request):
        return Response(
            {
                "message": "Welcome to the Pulse Check API",
                "available_endpoints": {
                    "admin": "/admin/",
                    "monitors": "/monitors/",
                    "openapi_schema": "/schema/",
                    "swagger_docs": "/schema/swagger-ui/",
                },
            },
            status=status.HTTP_200_OK,
        )