from django.shortcuts import render,get_object_or_404


from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, viewsets, mixins
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status

from apps.blogs import models
from apps.blogs import serializers
from apps.blogs.filters import BlogFilter
import json

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'


class BlogViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Blogs.objects.filter(data_status=0).order_by('id')
    # serializer_class = serializers.BlogListSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'slug'
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BlogFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BlogListSerializer
        return serializers.BlogSerializer

    def retrieve(self, request, *args, **kwargs):
        slug = kwargs['slug']
        queryset = models.Blogs.objects.filter(data_status=0).order_by('-id')
        blog = get_object_or_404(queryset, slug=slug)
        serializer = serializers.BlogSerializer(blog)
        # toc = eval(blog.toc)

        try:
            next_page = { 'slug': blog.get_next().slug,'title': blog.get_next().title,'status': 1 }
        except Exception as e:
            next_page = { 'slug': '#' ,'title': '阁下现在浏览的是最后一篇文章','status': 0}

        try:
            pre_page = { 'slug': blog.get_pre().slug,'title': blog.get_pre().title,'status': 1 }
        except Exception as e:
            pre_page = { 'slug': '#' ,'title': '阁下现在浏览的是第一篇文章','status': 0}

        context = {
            'blog': serializer.data,
            'next_page': next_page,
            'pre_page': pre_page

        }
        return Response(context)

class CategoriesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.BlogCategory.objects.filter(data_status=0).order_by('id')
    serializer_class = serializers.BlogCategoryListSerializer

class TagsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.BlogTags.objects.filter(data_status=0).order_by('id')
    serializer_class = serializers.BlogTagListSerializer