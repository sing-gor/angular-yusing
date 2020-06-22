from django.contrib import admin
from apps.blogs import models
# Register your models here.

@admin.register(models.Keywords)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('title','id',)


@admin.register(models.Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','slug','data_status')

@admin.register(models.BlogTags)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('title','slug','data_status')

@admin.register(models.BlogLogo)
class BlogLogoAdmin(admin.ModelAdmin):
    list_display = ('title','img',)

@admin.register(models.BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug','data_status')

# @admin.register(models.BlogTags)
# class BlogLinkTagAdmin(admin.ModelAdmin):
#     list_display = ('blog','blogtag',)

# @admin.register(BlogLinkLogo)
# class BlogLinkLogoAdmin(admin.ModelAdmin):
#     list_display = ('blog','bloglogo',)

# Register your models here.
