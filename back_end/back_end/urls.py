"""back_end URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.blogs import views as blog_views
from apps.toolbox import views as toolbox_views
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'blog', blog_views.BlogViewSet, basename='blogs')
router.register(r'category', blog_views.CategoriesViewSet, basename='category')
router.register(r'tags', blog_views.TagsViewSet, basename='tags')
router.register(r'sitedata', toolbox_views.MySiteDataViewSet, basename='mysites')
# router.register(r'blogtag', blog_views.BlogTagViewSet, basename='blogtag')
# router.register(r'blogcategory', blog_views.BlogCategoryViewSet,
#                 basename='blogcategory')
#
# router.register(r'sitedata', toolbox_views.MySiteDataViewSet,
#                 basename='mysites')
# router.register(r'friendlink', toolbox_views.FriendLinkViewSet,
#                 basename='friendlink')
# router.register(r'booklink', toolbox_views.BookLinkViewSet,
#                 basename='booklink')
# router.register(r'home', toolbox_views.HomeViewSet, basename='home')
# router.register(r'about', toolbox_views.AboutViewSet, basename='about')


urlpatterns = [


    path('api/', include(router.urls)),
    # re_path('^api-auth/', include('rest_framework.urls')),
    path('api/liuxinyi/', admin.site.urls),
    # re_path('^oauth/', include('social_django.urls', namespace='social')),

    # re_path('^api-token-auth/', obtain_jwt_token),
    # path('api/pageviews/', toolbox_views.PageviewsViewSet.as_view()),

    # re_path('^api-token-refresh/', refresh_jwt_token),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
