from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import serializers

from apps.blogs import models

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Keywords
        fields = ('title','desc')

class BlogTagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogTags
        fields = ('title','slug','body')



class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogTags
        exclude = ('id','data_status','keyword')

class BlogCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogCategory
        exclude = ('id','data_status','keyword')

# class BlogCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.BlogCategory
#         exclude = ('id','data_status')

class BlogLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogLogo
        fields = ('title','img')

class BlogListSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%B %d %Y')
    img = BlogLogoSerializer()
    class Meta:
        model = models.Blogs
        exclude = ('update_time','id','data_status','body','keyword','category','tags','script')


class BlogSerializer(serializers.ModelSerializer):
    tags = BlogTagSerializer(many=True)
    category = BlogCategoryListSerializer()
    keyword = KeywordSerializer()
    img = BlogLogoSerializer()
    created_time = serializers.DateTimeField(format='%B %d %Y')
    class Meta:
        model = models.Blogs
        exclude = ('update_time','id','data_status',)
