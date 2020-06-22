# Generated by Django 3.0.7 on 2020-06-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglogo',
            name='img',
            field=models.ImageField(upload_to='blog_img', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='blogtags',
            name='data_status',
            field=models.IntegerField(choices=[(0, '发布'), (1, '草稿')], default=1, verbose_name='是否发布'),
        ),
    ]
