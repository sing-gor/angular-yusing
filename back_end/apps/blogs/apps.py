from django.apps import AppConfig


class BlogsConfig(AppConfig):
    name = 'apps.blogs'
    label = 'blogs'
    def ready(self):
        from apps.blogs import signals
