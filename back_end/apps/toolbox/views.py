from django.shortcuts import render
from apps.toolbox import models,serializers
from rest_framework import generics, viewsets, mixins
from apps.toolbox import models,serializers
# Create your views here.
class MySiteDataViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.MySiteData.objects.all()
    serializer_class = serializers.MySiteDataSerializer
    # lookup_field = 'slug'

class HomeViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Home.objects.all()
    serializer_class = serializers.HomeSerializer

class AboutViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer

class FriendLinkViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.FriendLink.objects.all()
    serializer_class = serializers.FriendLinkSerializer



class BookLinkViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.BookLink.objects.all()
    serializer_class = serializers.BookLinkSerializer