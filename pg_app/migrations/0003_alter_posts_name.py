# Generated by Django 3.2.7 on 2021-09-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg_app', '0002_alter_posts_youtube_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='name',
            field=models.CharField(default='Dylan Guma', max_length=150),
        ),
    ]