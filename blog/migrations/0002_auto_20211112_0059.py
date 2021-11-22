# Generated by Django 3.2.9 on 2021-11-12 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=60, null=True, unique_for_date=models.DateTimeField(default=django.utils.timezone.now, null=True)),
        ),
        migrations.AlterField(
            model_name='post',
            name='auther',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='publish', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
