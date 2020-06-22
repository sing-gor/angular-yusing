from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.blogs import models
from apps.toolbox.models import MySiteData
#
#
# # def body_markdown(body):
#
#
# #     return body, toc
#
@receiver(post_save, sender=models.Blogs)
def blog_count(sender, instance, created, **kwargs):

    postsNum = models.Blogs.objects.filter(data_status=0).count()
    site_data = MySiteData.objects.filter(pk=1)[0]
    site_data.posts = postsNum
    site_data.save()


@receiver(post_save, sender=models.BlogTags)
def blog_tags_count(sender, instance, created, **kwargs):

    postsNum = models.BlogTags.objects.all().count()
    site_data = MySiteData.objects.filter(pk=1)[0]
    site_data.tags = postsNum
    site_data.save()


@receiver(post_save, sender=models.BlogCategory)
def blog_category_count(sender, instance, created, **kwargs):

    postsNum = models.BlogCategory.objects.all().count()
    site_data = MySiteData.objects.filter(pk=1)[0]
    site_data.categories = postsNum
    site_data.save()
