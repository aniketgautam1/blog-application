# Generated by Django 2.0.8 on 2019-08-27 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='created',
        ),
    ]
