from re import S
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""
    
    serializer_class = serializers.HelloSrializer
    
    def list(self, request):
        """Return a Hello Message"""
        a_viewset = [
            'bla bla bla',
            'bla bla bla bla bla'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """"Handle getting an object by id"""
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle partially updating an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'Delete'})
        

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
    