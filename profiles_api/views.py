from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Testing App View"""
    
    def get(self, request, format=None):
        """Returns a list of apiviews features"""
        
        an_apiview= [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over ur logic',
            'Maps manually to the urls'
        ]
        
        return Response({'message':'Hello ApiView','an_apiview':an_apiview})