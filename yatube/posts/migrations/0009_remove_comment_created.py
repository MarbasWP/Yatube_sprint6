# Generated by Django 2.2.6 on 2022-12-13 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20221213_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created',
        ),
    ]
