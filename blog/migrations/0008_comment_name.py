# Generated by Django 3.2.9 on 2021-11-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]