# Generated by Django 2.2 on 2019-09-10 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190910_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_views',
            field=models.IntegerField(default=0, max_length=10000),
        ),
    ]
