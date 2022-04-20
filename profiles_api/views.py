from re import S
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Testing App View"""
    
    serializer_class = serializers.HelloSrializer
    
    def get(self, request, format=None):
        """Returns a list of apiviews features"""
        
        an_apiview= [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over ur logic',
            'Maps manually to the urls'
        ]
        
        return Response({'message':'Hello ApiView','an_apiview':an_apiview})
    
    def post(self, request):
        """Create A Hello Message with our name"""
        
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """Handles Updating object"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """Handles Partially Updating object"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, p=None):
        """Deletes Object"""
        return Response({'method':'DELETE'})
    