from django_filters import rest_framework as filters

from django.db.models import Q
import django_filters

class BlogFilter(filters.FilterSet):
    tags = django_filters.CharFilter(method='touch_blog_tags')
    category = django_filters.CharFilter(method='touch_blog_category')



    def touch_blog_tags(self,queryset,name,value):
        return queryset.filter(tags__slug=value).distinct()


    def touch_blog_category(self,queryset,name,value):
        return queryset.filter(category__slug=value).distinct()
