from rest_framework import serializers

class HelloSrializer(serializers.Serializer):
    """Serilaizes  name field for testing our apiview"""
    
    name = serializers.CharField(max_length=10)