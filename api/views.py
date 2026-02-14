from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class GeneratePost(APIView):
    def get(self,req):
        return Response('hellow',status=status.HTTP_200_OK)
    def post(self,req):
        fields = req.data.fields
        return Response(fields,status=status.HTTP_201_CREATED)
        
