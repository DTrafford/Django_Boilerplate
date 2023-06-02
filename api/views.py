from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class GetRoutes(APIView):
    def get(self, request):
            routes = [
                {'GET':'/your_route/'},
                {'POST':'/your_route/'},
                {'GET':'/your_route/<id>/'},
                {'PUT':'/your_route/<id>/'},
                {'DELETE':'/your_route/<id>/'},
            ]
            return Response(routes)
    
    def post(self, request):
            return Response({"test": 1})