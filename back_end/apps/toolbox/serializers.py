from rest_framework import serializers

from apps.toolbox import models

class MySiteDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MySiteData
        exclude = ('id',)


class FriendLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FriendLink
        exclude = ('id',)


class BookLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookLink
        exclude = ('id',)

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Home
        exclude = ('id',)

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        exclude = ('id',)

class PageviewsSerializer(serializers.Serializer):
    slug = serializers.CharField(max_length=50)
    uuid = serializers.CharField(max_length=300)
