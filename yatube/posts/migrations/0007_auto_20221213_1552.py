# Generated by Django 2.2.6 on 2022-12-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_group_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/', verbose_name='Картинка'),
        ),
    ]
