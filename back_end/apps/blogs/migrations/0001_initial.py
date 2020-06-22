# Generated by Django 3.0.7 on 2020-06-15 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_status', models.IntegerField(choices=[(0, '发布'), (1, '草稿')], default=1, verbose_name='是否发布')),
                ('title', models.CharField(max_length=40, verbose_name='名称')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='索引')),
                ('body', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
                'db_table': 'blog_category',
            },
        ),
        migrations.CreateModel(
            name='BlogLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='名称')),
                ('img', models.ImageField(upload_to='blog_tags', verbose_name='图片')),
            ],
            options={
                'verbose_name': '图片logo',
                'verbose_name_plural': '图片logo',
                'db_table': 'blog_logos',
            },
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='该关键字用作SEO', max_length=200, verbose_name='文章关键字')),
                ('desc', models.TextField(default='s', verbose_name='简介')),
            ],
            options={
                'verbose_name': '关键字',
                'verbose_name_plural': '关键字',
                'db_table': 'keywords',
            },
        ),
        migrations.CreateModel(
            name='BlogTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_status', models.IntegerField(choices=[(0, 'font-awesome'), (1, 'svg')], default=1, verbose_name='icon-type')),
                ('title', models.CharField(max_length=40, verbose_name='名称')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='索引')),
                ('body', models.TextField(verbose_name='内容')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Keywords', verbose_name='關鍵字')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
                'db_table': 'blog_tags',
            },
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_status', models.IntegerField(choices=[(0, '发布'), (1, '草稿')], default=1, verbose_name='是否发布')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('body', models.TextField(verbose_name='内容')),
                ('author', models.CharField(default='Sing', max_length=50, verbose_name='作者')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('slug', models.SlugField(unique=True, verbose_name='索引后缀')),
                ('script', models.TextField(default='s', verbose_name='javascript')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.BlogCategory', verbose_name='文章分類')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.BlogLogo', verbose_name='图片关联')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Keywords', verbose_name='關鍵字')),
                ('tags', models.ManyToManyField(to='blogs.BlogTags', verbose_name='文章標籤')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章列表',
                'db_table': 'blogs',
                'ordering': ['-created_time'],
            },
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Keywords', verbose_name='關鍵字'),
        ),
    ]
