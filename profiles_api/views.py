from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import status
from profiles_api import serializers
from profiles_api import models

#for login api
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.
class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HellloSerializer
    
    def get(self, request, format = None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the mostcontrol over your application logic',
            'Is mapped manuualyto URLs',    
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self, request):
        """Create a hello message with your name"""
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
            
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle the partial update of an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    """Test Api Viewset"""
    
    serializer_class = serializers.HellloSerializer
    
    def list(self, request):
        """Returns a hello message"""
        
        a_viewset = [
            'Uses action (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'provies more functinality with less codes'
        ]
        
        return(Response({'message':'Hello!','a_viewset':a_viewset}))
    
    def create(self, request):
        """Create a new Hello!! message"""
        
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}!!"
            return Response({'message':message})
        else:
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST

    def retrive(self, request, pk = None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})
    
    def update(self, request, pk = None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk = None):
        """Handle updating a part of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk = None):
        """Handal removing and objects"""
        return Response({'http_method':'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
    
class UserLoginViewApi(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnProfile,
        IsAuthenticated
    )
    
    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)